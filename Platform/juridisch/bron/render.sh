#!/usr/bin/env bash
# Rendert de HTML-bronnen naar PDF in Platform/juridisch/.
set -euo pipefail
cd "$(dirname "$0")"
CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
for f in privacy-statement terms-of-service; do
  "$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="../eduface-$f.pdf" "file://$PWD/$f.html" 2>/dev/null
done
