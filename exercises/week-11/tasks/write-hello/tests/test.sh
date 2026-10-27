#!/usr/bin/env bash
set -euo pipefail
APP_DIR="${APP_DIR:-/app}"
LOGS_DIR="${LOGS_DIR:-/logs/verifier}"
mkdir -p "$LOGS_DIR"
# TODO: if "$APP_DIR/out.txt" is exactly hello + newline, write 1 else 0
# to "$LOGS_DIR/reward.txt"
echo 0 > "$LOGS_DIR/reward.txt"
