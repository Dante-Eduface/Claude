#!/bin/zsh
# Test of een launchd-proces bij de projectmap kan.
#
#   zsh .claude/scripts/shift-rechten-check.sh
#
# Waarom dit bestaat: op 17-09-2026 draaide de nachtronde wel, maar kon hij
# pipeline.py niet openen ("Operation not permitted"). Een launchd-proces valt
# onder de privacyregels van macOS en heeft geen toegang tot deze map, ook niet
# als jij er in Finder gewoon bij kunt. Het gevolg was een ronde die uren liep
# en niets opleverde.
#
# Dit script start een tijdelijke launchd-taak die precies test wat de
# nachtronde nodig heeft, en ruimt zichzelf daarna op.

set -u

P="/Users/User/Library/CloudStorage/GoogleDrive-dante.torbed@eduface.me/My Drive/Eduface/Claud AE"
WERK="$HOME/Library/Application Support/eduface"
LOG="$HOME/Library/Logs/eduface-rechten-check.log"
PLIST="$HOME/Library/LaunchAgents/me.eduface.rechtencheck.plist"

mkdir -p "$WERK"
cat > "$WERK/rechten-check.sh" <<'INNER'
#!/bin/zsh
P="/Users/User/Library/CloudStorage/GoogleDrive-dante.torbed@eduface.me/My Drive/Eduface/Claud AE"
L="$HOME/Library/Logs/eduface-rechten-check.log"
: > "$L"
cd "$P" 2>/dev/null && print "map openen      ok" >> "$L" || print "map openen      GEWEIGERD" >> "$L"
cat "$P/GTM/Campaigns/shift/master/orgs.csv" > /dev/null 2>/dev/null \
  && print "gegevens lezen  ok" >> "$L" || print "gegevens lezen  GEWEIGERD" >> "$L"
print x > "$P/GTM/Campaigns/shift/master/.rechten-probe" 2>/dev/null \
  && { print "gegevens schrijven ok" >> "$L"; rm -f "$P/GTM/Campaigns/shift/master/.rechten-probe" } \
  || print "gegevens schrijven GEWEIGERD" >> "$L"
python3 "$P/.claude/scripts/pipeline.py" --markt uk status > /dev/null 2>/dev/null \
  && print "pipeline.py     ok" >> "$L" || print "pipeline.py     GEWEIGERD" >> "$L"
git -C "$P/GTM/Campaigns/shift" status --short > /dev/null 2>/dev/null \
  && print "git             ok" >> "$L" || print "git             GEWEIGERD" >> "$L"
print "KLAAR" >> "$L"
INNER
chmod +x "$WERK/rechten-check.sh"

cat > "$PLIST" <<XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>me.eduface.rechtencheck</string>
  <key>ProgramArguments</key>
  <array><string>/bin/zsh</string><string>$WERK/rechten-check.sh</string></array>
  <key>RunAtLoad</key><true/>
</dict>
</plist>
XML

rm -f "$LOG"
launchctl unload "$PLIST" 2>/dev/null
launchctl load "$PLIST" 2>/dev/null

print "Even geduld, de test draait..."
for i in {1..30}; do
  [[ -f "$LOG" ]] && grep -q KLAAR "$LOG" 2>/dev/null && break
  sleep 1
done

print ""
if [[ -f "$LOG" ]]; then
  grep -v KLAAR "$LOG"
  print ""
  if grep -q GEWEIGERD "$LOG"; then
    print "Zoals verwacht: een launchd-taak komt hier niet bij."
    print ""
    print "Dit is GEEN probleem meer, en het is ook niet op te lossen met"
    print "Volledige schijftoegang voor /bin/zsh: dat is geprobeerd op 17-09-2026"
    print "en macOS geeft dat recht alleen aan echte programma's, niet aan een"
    print "kale shell. De vinkjes stonden aan en de test bleef falen."
    print ""
    print "De nachtronde loopt daarom via een geplande taak in de Claude-app"
    print "(zijbalk, Scheduled). Die draait in dezelfde context als een gewoon"
    print "gesprek en heeft de rechten dus wel. Voorwaarde: de app staat open."
    print ""
    print "Dit script is alleen nog een diagnose, geen taak die af moet."
  else
    print "Alles toegankelijk vanuit launchd. Dat is ongebruikelijk; als dit"
    print "klopt zou de nachtronde ook zonder de Claude-app kunnen draaien."
  fi
else
  print "De test leverde geen log op. Draait launchd wel?"
fi

launchctl unload "$PLIST" 2>/dev/null
rm -f "$PLIST"
