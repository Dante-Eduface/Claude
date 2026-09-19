#!/bin/zsh
# doctor.sh — checkt of deze machine de skill kan draaien. Mechanisch, geen model.
# Draai dit VOORDAT je iets belooft. Lane A heeft bijna niets nodig, Lane B heeft ffmpeg.
OK=0
say() { printf "%-16s %s\n" "$1" "$2" }
need() { if command -v $1 >/dev/null 2>&1; then say "$1" "ok  $(command -v $1)"; else say "$1" "ONTBREEKT $2"; OK=1; fi }

echo "--- Lane A (pure-code, altijd beschikbaar) ---"
need node ""
[[ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]] \
  && say "chrome" "ok" || { say "chrome" "ONTBREEKT (nodig voor verify.js/shot.js)"; OK=1; }
PUP="$(cd "$(dirname $0)/../../../.." && pwd)/projects/website-building/node_modules/puppeteer-core"
[[ -d "$PUP" ]] && say "puppeteer-core" "ok  (gedeeld: projects/website-building)" \
  || { say "puppeteer-core" "ONTBREEKT -> npm i puppeteer-core in projects/website-building"; OK=1; }

echo "\n--- Lane B (echte video, alleen als Dante dat wil) ---"
need python3 ""
need ffmpeg "-> brew install ffmpeg"
need ffprobe "-> brew install ffmpeg"
need xxd ""
command -v higgsfield >/dev/null 2>&1 && say "higgsfield" "ok" || say "higgsfield" "niet geinstalleerd (Kie-pad of Lane A gebruiken)"
[[ -n "$KIE_API_KEY" || -r "$HOME/.config/kie/key" ]] && say "kie key" "ok" || say "kie key" "geen key (Lane B via Kie kan niet)"

echo "\n--- Publiceren ---"
command -v vercel >/dev/null 2>&1 && say "vercel" "ok" || say "vercel" "niet geinstalleerd (Eduface publiceert via Framer, meestal niet nodig)"

echo ""
if (( OK == 0 )); then echo "Lane A is groen."; else echo "Lane A mist iets hierboven, los dat eerst op."; fi
