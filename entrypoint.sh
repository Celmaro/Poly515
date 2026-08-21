#!/bin/sh
set -e
echo "Poly515 wrapper: running precheck..." >&2
python precheck.py
echo "Poly515 wrapper: precheck done, starting bot..." >&2
exec python bot.py --test-mode --no-grafana
