#!/bin/zsh
# Nachtronde van de SHIFT-pijplijn. Draait agent 1 tot en met 4 en laat 's ochtends
# een wachtrij met concepten achter. Zet nooit iets naar buiten: de grendel-hook
# .claude/hooks/shift-nacht-grendel.py blokkeert elke verstuur-, import- en
# credit-tool zolang SHIFT_NACHT=1 staat.
#
# Bron van waarheid is dit bestand in de repo. launchd draait de KOPIE in
# ~/Library/Application Support/eduface/, want launchd start niet vanaf een
# Google-Drive-pad. Wijzig je hier iets, dan draait de nacht nog de oude versie
# tot je kopieert:
#     zsh .claude/scripts/run-shift-nacht.sh --installeer
#
# De instellingen van de nachtelijke run (welke agents, welke markt, hoeveel
# uur) staan NIET hier maar in de plist, onder EnvironmentVariables:
#     ~/Library/LaunchAgents/me.eduface.shift.plist
# Na een wijziging daar: launchctl unload en load, anders blijft de oude gelden.
#
# Elke agent is een eigen claude-aanroep met een eigen tijdslimiet. Als agent 1
# vastloopt draaien 2, 3 en 4 gewoon door, en het log blijft leesbaar.

set -u

PROJECT="/Users/User/Library/CloudStorage/GoogleDrive-dante.torbed@eduface.me/My Drive/Eduface/Claud AE"
LOG="$HOME/Library/Logs/eduface-shift-nacht.log"
STATUSBESTAND="$PROJECT/GTM/ICP/shift/NACHTRUN.md"

# Wat er per ronde gebeurt. Bescheiden gehouden: een ronde die te veel wil doet
# niets af, en agent 1 en 3 zijn traag omdat ze het web op moeten.
# Per aanroep werkt een agent een batch af. Daarna roepen we hem opnieuw aan,
# net zolang tot hij niets meer toevoegt of het tijdbudget op is. De batch is
# dus geen doel maar een portie: hij houdt de context van een agent-sessie
# hanteerbaar en zorgt dat een systematische fout na een batch zichtbaar is
# in plaats van na driehonderd records.
MARKT="${SHIFT_MARKT:-uk}"
N_ORGS="${SHIFT_N_ORGS:-15}"          # agent 1: organisaties per batch
N_CONTACTEN="${SHIFT_N_CONTACTEN:-15}"
N_ONDERZOEK="${SHIFT_N_ONDERZOEK:-10}"
N_BERICHTEN="${SHIFT_N_BERICHTEN:-10}"
MINUTEN_PER_AGENT="${SHIFT_MINUTEN:-45}"   # tijdslimiet per losse aanroep

# Tot hoe laat de ronde mag doorwerken. Een klok-eindtijd en niet een duur,
# want een duur telt slaaptijd mee: op 17-09-2026 startte de ronde om 02:00,
# sliep de Mac vijf uur, en begon agent 1 om 07:03 drie minuten NA zijn eigen
# deadline. Met een eindtijd maakt het niet uit wanneer de machine wakker wordt.
STOP_UUR="${SHIFT_STOP_UUR:-8}"

# Wordt de Mac laat wakker, dan is de eindtijd al gepasseerd en zou de ronde
# niets doen. Daarom altijd minimaal deze tijd werken vanaf het echte begin.
MIN_MINUTEN="${SHIFT_MIN_MINUTEN:-60}"

# Welke agents er deze ronde mogen draaien. Nuttig terwijl je aan een skill
# werkt: zet agent 1 en 2 aan om voorraad op te bouwen, en laat 3 en 4 uit tot
# hun skill staat zoals je hem wilt. Anders schrijft agent 4 vannacht honderd
# berichten volgens een skill die je morgen omgooit.
#   SHIFT_AGENTS="1,2" zsh run-shift-nacht.sh
AGENTS="${SHIFT_AGENTS:-1,2,3,4}"
doet() { [[ ",$AGENTS," == *",$1,"* ]] }
MAX_BATCHES="${SHIFT_MAX_BATCHES:-40}"     # noodrem tegen een lus die blijft tikken

mkdir -p "$HOME/Library/Logs"
log() { print -r -- "$(date '+%Y-%m-%d %H:%M:%S') $*" >> "$LOG" }

# --droog: loop de hele ronde door zonder iets te starten of te schrijven.
# Bedoeld om te zien WAT er gaat gebeuren: welke commando's, welke prompts naar
# welke agent, in welke volgorde. Kost niets en raakt het master-document niet.
DROOG=0
[[ "${1:-}" == "--droog" ]] && { DROOG=1; shift }

# --installeer: kopieer dit script naar de plek waar launchd het kan starten
if [[ "${1:-}" == "--installeer" ]]; then
  DOEL="$HOME/Library/Application Support/eduface"
  mkdir -p "$DOEL"
  cp "$0" "$DOEL/run-shift-nacht.sh" && chmod +x "$DOEL/run-shift-nacht.sh"
  print -r -- "gekopieerd naar $DOEL/run-shift-nacht.sh"
  exit 0
fi

log "===== ronde start (markt $MARKT, agents $AGENTS) ====="

CLAUDE=$(ls -dt "$HOME/.vscode/extensions/anthropic.claude-code-"*/resources/native-binary/claude 2>/dev/null | head -1)
[[ -x "${CLAUDE:-}" ]] || CLAUDE=$(command -v claude 2>/dev/null)

# Elke afbreking schrijft hetzelfde statusbestand, zodat een stille nacht niet
# als een geslaagde nacht leest. De hot-leads-job faalde twee runs op een
# verlopen sessie zonder dat iemand het merkte; dat is de reden dat dit bestaat.
afbreken() {
  log "AFGEBROKEN: $1"
  cat > "$STATUSBESTAND" <<EOF
# Nachtronde SHIFT

**$(date '+%d-%m-%Y %H:%M') - MISLUKT**

$1

Log: \`$LOG\`
EOF
  osascript -e "display notification \"$1\" with title \"SHIFT-nachtronde mislukt\"" 2>/dev/null
  log "===== ronde einde (mislukt) ====="
  exit 1
}

[[ -n "${CLAUDE:-}" && -x "$CLAUDE" ]] || afbreken "claude-binary niet gevonden"
cd "$PROJECT" || afbreken "kan niet in de projectmap (Drive niet gekoppeld?)"

# Geheimen komen uit een bestand buiten de repo en buiten Google Drive.
# launchd geeft een kale omgeving mee, dus zonder dit staat er niets klaar.
# Zet het token er een keer in met:
#   install -m 600 /dev/null "$HOME/Library/Application Support/eduface/shift.env"
#   printf 'export CLAUDE_CODE_OAUTH_TOKEN=%s\n' '<token>' >> ...datzelfde pad
GEHEIMEN="$HOME/Library/Application Support/eduface/shift.env"
if [[ -f "$GEHEIMEN" ]]; then
  source "$GEHEIMEN"
  log "geheimen geladen uit $GEHEIMEN"
fi

# Voor we een halve nacht verstoken: is de sessie uberhaupt ingelogd?
# `auth status` kost geen tokens en geen API-call, in tegenstelling tot een
# proef-prompt. Het antwoord is JSON met een veld loggedIn. De newlines gaan
# eruit, want een meerregelige melding breekt de quoting van afbreken().
AUTH=$("$CLAUDE" auth status 2>&1 | tr -d '\n' | tr -s ' ')
if (( DROOG )); then
  print "DROGE RONDE, markt $MARKT. Er wordt niets gestart en niets geschreven."
  print "Hieronder staat per agent de prompt die hij anders had gekregen."
  [[ "$AUTH" == *'"loggedIn": true'* || -n "${CLAUDE_CODE_OAUTH_TOKEN:-}" ]] \
    && print "Inloggen: in orde." || print "Inloggen: NIET in orde, een echte ronde zou hier stoppen."
elif [[ "$AUTH" != *'"loggedIn": true'* && -z "${CLAUDE_CODE_OAUTH_TOKEN:-}" ]]; then
  afbreken "claude is niet ingelogd en er staat geen CLAUDE_CODE_OAUTH_TOKEN in $GEHEIMEN. Maak een token van een jaar met: $CLAUDE setup-token -- en zet de regel export CLAUDE_CODE_OAUTH_TOKEN=... in dat bestand (chmod 600). Een gewone sessie volstaat ook: $CLAUDE auth login, maar die verloopt binnen een uur en dat is precies waarom deze job eerder wekenlang stil faalde. Status nu: ${AUTH:0:120}"
fi
if [[ -n "${CLAUDE_CODE_OAUTH_TOKEN:-}" ]]; then
  export CLAUDE_CODE_OAUTH_TOKEN
  log "langlevend token in gebruik"
fi

(( DROOG )) || git -C "$PROJECT/GTM/ICP/shift" pull --quiet --rebase 2>>"$LOG" \
  || log "let op: git pull mislukte, ga door"

export SHIFT_NACHT=1          # zet de grendel-hook aan
export SHIFT_MARKT="$MARKT"

# perl levert de tijdslimiet: macOS heeft geen timeout(1)
draai() {
  local naam="$1" prompt="$2"
  log "-- $naam"
  if (( DROOG )); then
    print ""
    print "================================================================"
    print "  $naam"
    print "================================================================"
    print -r -- "$prompt"
    print ""
    return 0
  fi
  /usr/bin/perl -e 'alarm shift; exec @ARGV' $((MINUTEN_PER_AGENT * 60)) \
    "$CLAUDE" -p "$prompt" \
      --model sonnet \
      --permission-mode bypassPermissions \
      --output-format text >> "$LOG" 2>&1
  local rc=$?
  [[ $rc -eq 0 ]] || log "   $naam eindigde met code $rc (gaat door met de volgende)"
}

# De late van twee momenten: vandaag om STOP_UUR, of nu plus MIN_MINUTEN.
EINDTIJD=$(date -j -f "%Y-%m-%d %H:%M:%S" "$(date '+%Y-%m-%d') $(printf '%02d' $STOP_UUR):00:00" +%s 2>/dev/null || print 0)
MINIMAAL=$(( $(date +%s) + MIN_MINUTEN * 60 ))
DEADLINE=$(( EINDTIJD > MINIMAAL ? EINDTIJD : MINIMAAL ))
log "werkt door tot $(date -r $DEADLINE '+%H:%M')"

# Hoeveel werk staat er nog voor deze stap? Uit pipeline.py, want die kent de
# stand; het script rekent zelf niets uit.
meet() {
  python3 .claude/scripts/pipeline.py --markt "$MARKT" status 2>/dev/null \
    | python3 -c "import json,sys; print(json.load(sys.stdin).get('$1', 0))" 2>/dev/null || print 0
}

# Roep een agent aan tot hij niets meer verandert of de tijd op is.
# De stopvoorwaarde is expres "geen voortgang" en niet "wachtrij leeg": een
# agent die vastloopt op een record dat hij niet kan oplossen, zou anders
# eindeloos dezelfde batch blijven proberen.
draai_tot_klaar() {
  local naam="$1" prompt="$2" maatstaf="$3" batch=0
  while (( batch < MAX_BATCHES )); do
    if (( $(date +%s) >= DEADLINE )) && (( ! DROOG )); then
      log "   $naam gestopt: eindtijd $(date -r $DEADLINE '+%H:%M') bereikt na $batch batch(es)"
      break
    fi
    local voor=$(meet "$maatstaf")
    draai "$naam (batch $(( batch + 1 )))" "$prompt"
    (( batch++ ))
    (( DROOG )) && break                  # droog: een keer laten zien is genoeg
    local na=$(meet "$maatstaf")
    if [[ "$voor" == "$na" ]]; then
      log "   $naam klaar: $maatstaf bleef op $na staan na batch $batch"
      break
    fi
    log "   $naam batch $batch: $maatstaf van $voor naar $na"
  done
}

BASIS="Lees eerst je eigen leerpuntenbestand: LEERPUNTEN.md in je skillmap, of
.claude/agents/LEERPUNTEN-shift-research.md als je agent 3 bent. Daar staat wat er eerder is
gecorrigeerd en waarom. Zonder dat maak je vannacht dezelfde fout als vorige week.

Je schrijft alleen naar het master-document via python3 .claude/scripts/pipeline.py met
--markt $MARKT. Je stelt geen vragen, er is niemand wakker: kom je er niet uit bij een record,
zet dan notities of twijfels op dat record en ga door met het volgende.

Loop je tegen iets aan wat structureel lijkt, dus niet dit ene record maar de manier waarop
je werkt, zet dat dan als regel in je eigen leerpuntenbestand met de datum en wat je zag.
Dante leest die 's ochtends."

# Alleen agent 4 komt in de buurt van iets dat de deur uit kan, dus alleen daar
# hoort die grens. Bij agent 1 tot en met 3 was het ruis: die raken Lemlist niet
# aan en een verbod op iets wat je toch niet doet leest als achtergrondgeluid.
GRENZEN="$BASIS"
GRENZEN_4="$BASIS

Je laat bericht_status op concept staan. Goedkeuren doet Dante, en importeren in Lemlist
gebeurt daarna met de hand. Voeg zelf niets toe aan een campagne en verstuur niets."

doet 1 && draai_tot_klaar "agent 1 lead-sourcing" "Gebruik de skill lead-sourcing voor markt $MARKT. Zoek $N_ORGS nieuwe organisaties die binnen de ICP vallen en zet ze met bewijs in het master-document. Dit is een batch, niet het doel: je wordt hierna opnieuw aangeroepen tot de bronnen op zijn. Werk daarom je bronnenlijst systematisch af en houd in de werkvoorraad bij waar je gebleven bent, zodat de volgende batch verder gaat in plaats van opnieuw te beginnen. Vind je niets nieuws meer, zeg dat dan expliciet. $GRENZEN" "orgs_totaal"

doet 2 && draai_tot_klaar "agent 2 contact-sourcing" "Gebruik de skill contact-sourcing voor markt $MARKT. Werk $N_CONTACTEN organisaties uit de wachtrij van stage 2 af (python3 .claude/scripts/pipeline.py --markt $MARKT queue --stage 2). Dit is een batch, niet het doel: je wordt hierna opnieuw aangeroepen tot de wachtrij leeg is. $GRENZEN" "stage_2_orgs_zonder_contact"

doet 3 && draai_tot_klaar "agent 3 onderzoek" "Gebruik de subagent shift-research voor markt $MARKT. Onderzoek $N_ONDERZOEK personen uit de wachtrij van stage 3 (python3 .claude/scripts/pipeline.py --markt $MARKT queue --stage 3). Dit is een batch, niet het doel: je wordt hierna opnieuw aangeroepen tot de wachtrij leeg is. $GRENZEN" "stage_3_onderzoek"

doet 4 && draai_tot_klaar "agent 4 berichten" "Gebruik de skill outreach voor markt $MARKT. Schrijf voor maximaal $N_BERICHTEN personen uit de wachtrij van stage 4 (python3 .claude/scripts/pipeline.py --markt $MARKT queue --stage 4) de berichten. $GRENZEN_4" "stage_4_bericht_schrijven"

# Terugschrijven wat er in de campagne gebeurde, en dan pas rekenen.
# Dit moet via een claude-sessie: Lemlist is alleen bereikbaar via de
# claude.ai-connector, de REST API geeft op dit account 403 op elk endpoint.
LEADS="${TMPDIR%/}/shift-lemlist-$MARKT.json"
draai "sync-lemlist" "Werk de meetlus bij voor markt $MARKT. Doe dit in twee stappen, want de
tweede is duur en de eerste is bijna gratis.

STAP 1, de peiling. Lees de campagne-id uit GTM/ICP/shift/markets/$MARKT/profiel.json
(lemlist_campagne_id). Is die leeg, meld dat en stop. Draai anders get_campaigns_stats op die
campagne en tel drie getallen op: messageMetrics.sent, channelMetrics.linkedinInvitationAccepted
en messageMetrics.replied. Geef die door aan:
  python3 .claude/scripts/pipeline.py --markt $MARKT peiling --verstuurd N --geaccepteerd N --gereageerd N
Zegt dat commando ophalen_nodig=false, dan ben je klaar. Meld dat er niets veranderd is en stop.

STAP 2, alleen als de peiling zegt dat het nodig is. Haal met search_campaign_leads alle leads
op met include=[\"activities\"] en limit=10 per aanroep, pagineer met offset tot hasMore false is.
Grotere batches kappen het activities-veld af, dus houd het op 10. Schrijf alles als JSON-array
naar $LEADS met een Python-script (json.dump, ensure_ascii=False) en draai:
  python3 .claude/scripts/pipeline.py --markt $MARKT sync-lemlist --invoer $LEADS
Draai daarna dezelfde peiling nog een keer met --leg-vast erbij, zodat de volgende nacht weet
waar hij stond.

Alleen leesacties op Lemlist. Voeg niets toe, verstuur niets, wijzig geen campagne."
SYNC=$(python3 .claude/scripts/pipeline.py --markt "$MARKT" rapport --table 2>&1 | head -4)

log "-- doctor"
if (( DROOG )); then
  print "================================================================"
  print "  daarna draait de ronde deze commando's"
  print "================================================================"
  print "  python3 .claude/scripts/pipeline.py --markt $MARKT doctor --fix-safe"
  print "  python3 .claude/scripts/pipeline.py --markt $MARKT status --table"
  print "  python3 .claude/scripts/pipeline.py --markt $MARKT rapport --table"
  print "  python3 .claude/scripts/pipeline.py --markt $MARKT cockpit --out /tmp/cockpit-$MARKT.json"
  print "  git add, commit en push in GTM/ICP/shift"
  print "  stand naar GTM/ICP/shift/NACHTRUN.md"
  print ""
  print "Droge ronde klaar. Er is niets gestart en niets gewijzigd."
  log "===== droge ronde einde ====="
  exit 0
fi
DOC=$(python3 .claude/scripts/pipeline.py --markt "$MARKT" doctor --fix-safe 2>&1 | head -40)
print -r -- "$DOC" >> "$LOG"

STAND=$(python3 .claude/scripts/pipeline.py --markt "$MARKT" status --table 2>&1)
RAPPORT=$(python3 .claude/scripts/pipeline.py --markt "$MARKT" rapport --table 2>&1)

git -C "$PROJECT/GTM/ICP/shift" add -A >>"$LOG" 2>&1
git -C "$PROJECT/GTM/ICP/shift" commit -q -m "Nachtronde $(date '+%d-%m-%Y'), markt $MARKT" >>"$LOG" 2>&1 \
  && git -C "$PROJECT/GTM/ICP/shift" push --quiet >>"$LOG" 2>&1 \
  || log "niets te committen of push mislukt"

cat > "$STATUSBESTAND" <<EOF
# Nachtronde SHIFT

**$(date '+%d-%m-%Y %H:%M') - klaar** (markt $MARKT)

## Stand van de trechter
\`\`\`
$STAND
\`\`\`

## Werkt het, en voor wie
\`\`\`
$RAPPORT
\`\`\`

## Controle
\`\`\`
$DOC
\`\`\`

Volgende stap: de concepten van stage 4 nakijken en goedkeuren in de cockpit, daarna
\`/lemlist-import\` voor markt $MARKT.
EOF

log "===== ronde einde (klaar) ====="
