#!/usr/bin/env bash
set -euo pipefail
APP_DIR="${APP_DIR:-/app}"
LOGS_DIR="${LOGS_DIR:-/logs/verifier}"
mkdir -p "$LOGS_DIR"
HERE="$(cd "$(dirname "$0")" && pwd)"
# Tests are copied in at verify time. Do not assume they lived in APP_DIR
# during the agent phase.
if pytest "$HERE/test_clamp.py" -q; then
  echo 1 > "$LOGS_DIR/reward.txt"
else
  echo 0 > "$LOGS_DIR/reward.txt"
fi
