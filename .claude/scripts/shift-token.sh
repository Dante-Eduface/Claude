#!/bin/zsh
# Zet het langlevende Claude-token in het geheimenbestand van de nachtronde.
#
#   zsh .claude/scripts/shift-token.sh          maakt zelf een nieuw token aan
#   zsh .claude/scripts/shift-token.sh --plak   je plakt een token dat je al hebt
#
# Standaard draait dit script `claude setup-token` voor je, vangt het token uit
# de uitvoer op en schrijft het meteen weg. Jij hoeft alleen in de browser op
# autoriseren te klikken. Zo hoeft het token nergens door een plakbord of een
# chatvenster, en kan de placeholder-fout niet meer gebeuren.

set -u

GEHEIMEN="$HOME/Library/Application Support/eduface/shift.env"
CLAUDE=$(ls -dt "$HOME/.vscode/extensions/anthropic.claude-code-"*/resources/native-binary/claude 2>/dev/null | head -1)
[[ -x "${CLAUDE:-}" ]] || CLAUDE=$(command -v claude 2>/dev/null)
if [[ -z "${CLAUDE:-}" || ! -x "$CLAUDE" ]]; then
  print -u2 "Geen claude-binary gevonden onder ~/.vscode/extensions."
  exit 1
fi

opslaan() {
  local token="$1"
  mkdir -p "$(dirname "$GEHEIMEN")"
  [[ -f "$GEHEIMEN" ]] || { install -m 600 /dev/null "$GEHEIMEN"
    print '# Geheimen voor de SHIFT-nachtronde. Buiten git, buiten Google Drive.' >> "$GEHEIMEN" }
  grep -v '^export CLAUDE_CODE_OAUTH_TOKEN=' "$GEHEIMEN" > "$GEHEIMEN.tmp" 2>/dev/null || true
  print "export CLAUDE_CODE_OAUTH_TOKEN=$token" >> "$GEHEIMEN.tmp"
  mv "$GEHEIMEN.tmp" "$GEHEIMEN"
  chmod 600 "$GEHEIMEN"
  print "Opgeslagen in $GEHEIMEN (alleen leesbaar voor jou)."

  print -n "Controle: "
  if CLAUDE_CODE_OAUTH_TOKEN="$token" "$CLAUDE" auth status 2>&1 | grep -q '"loggedIn": true'; then
    print "ingelogd. De nachtronde kan draaien:"
    print "  zsh .claude/scripts/run-shift-nacht.sh"
    return 0
  fi
  print "Claude zegt nog steeds niet ingelogd. Het token is wel opgeslagen;"
  print "mogelijk is het onvolledig. Draai dit script anders opnieuw."
  return 1
}

geldig() {
  local t="$1"
  [[ -n "$t" && "$t" != "PLAK_HIER" && "$t" != *"<"*">"* && ${#t} -ge 20 ]]
}

if [[ "${1:-}" == "--plak" ]]; then
  print "Plak het token en druk twee keer op enter. Je ziet niets verschijnen."
  print "Loopt het token over meer dan een regel, plak dan gewoon alles."
  TOKEN=""
  while true; do
    read -s REGEL || break
    [[ -z "$REGEL" ]] && break
    TOKEN="$TOKEN$REGEL"
  done
  print ""
  TOKEN="${TOKEN#export CLAUDE_CODE_OAUTH_TOKEN=}"
  TOKEN="${TOKEN//[[:space:]]/}"
  geldig "$TOKEN" || { print -u2 "Dat is geen bruikbaar token. Er is niets gewijzigd."; exit 1 }
  opslaan "$TOKEN"
  exit $?
fi

print "Er opent zo een browser. Klik daar op autoriseren en kom terug;"
print "het token wordt hier opgevangen en opgeslagen, je hoeft niets te kopieren."
print ""

UITVOER=$("$CLAUDE" setup-token 2>&1 | tee /dev/tty)

# Het token staat tussen "Your OAuth token" en "Store this token", en de
# terminal breekt het over TWEE regels af. Die moeten weer aan elkaar, anders
# sla je de helft op en faalt het pas bij de eerste nachtronde.
# Alleen regels die na het trimmen uit een enkel lang woord bestaan. Zinnen
# eromheen hebben spaties en vallen af; de twee tokenregels niet.
TOKEN=$(print -r -- "$UITVOER" \
  | tr -d '\r' \
  | sed -n '/Your OAuth token/,/Store this token/p' \
  | sed 's/^[[:space:]]*//; s/[[:space:]]*$//' \
  | grep -E '^[A-Za-z0-9_-]{20,}$' \
  | tr -d '\n')

if ! geldig "${TOKEN:-}"; then
  print ""
  print -u2 "Kon het token niet uit de uitvoer halen."
  print -u2 "Kopieer het hierboven met de hand en draai dan:"
  print -u2 "  zsh .claude/scripts/shift-token.sh --plak"
  exit 1
fi

print ""
opslaan "$TOKEN"
