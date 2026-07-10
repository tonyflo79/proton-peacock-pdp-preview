#!/bin/bash
# render.sh <html-file> <out-png>  — renders a 2048x2048 composite via headless Chrome
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="$(cd "$(dirname "$0")" && pwd)"
HTML="$1"; OUT="$2"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=1 --window-size=2048,2048 \
  --default-background-color=FFFFFFFF --virtual-time-budget=9000 \
  --screenshot="$OUT" "file://$DIR/$HTML" 2>/dev/null
echo "rendered -> $OUT"
