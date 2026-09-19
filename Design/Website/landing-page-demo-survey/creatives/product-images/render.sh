#!/bin/zsh
# Rendert alle frames op 2x. Chrome hangt op de Drive-mount, dus eerst naar een lokale map.
set -e
HERE="${0:A:h}"
TMP="$(mktemp -d /tmp/eduface-frames.XXXX)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
render() { # naam bodyclass breedte hoogte bronbestand
  local name=$1 cls=$2 w=$3 h=$4 src=$5
  sed "s/<body class=\"[a-z ]*\">/<body class=\"$cls\">/" "$HERE/$src" > "$TMP/$name.html"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 --default-background-color=00000000 \
    --window-size=$w,$h --virtual-time-budget=4000 --screenshot="$TMP/$name.png" "file://$TMP/$name.html" 2>/dev/null
  cp "$TMP/$name.png" "$HERE/$name.png"; echo "  $name.png"
}
python3 "$HERE/gen.py" >/dev/null
for s in law economics social-sciences stem humanities health-sciences; do
  render "paper-grader-$s" plain 1520 628 "paper-grader-$s.html"
done
# nummers bij de drie titels, voor de how-it-works-sectie
render "paper-grader-economics-callouts" callouts 1520 628 "paper-grader-economics.html"
render "exam-grader" plain 1520 700 "exam-grader.html"
render "hero" plain 1560 660 "hero.html"
rm -rf "$TMP"
