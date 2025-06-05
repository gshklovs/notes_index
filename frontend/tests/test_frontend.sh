#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="${SCRIPT_DIR}/.."
cd "$PROJECT_ROOT"

npm install >/dev/null
npx vite build >/dev/null
npx vite preview --port 3000 >/tmp/vite_test.log 2>&1 &
PID=$!

cleanup() {
  kill $PID
}
trap cleanup EXIT

for i in {1..15}; do
  if curl -s http://localhost:3000 | grep -q "Hello World"; then
    echo "Frontend test passed"
    exit 0
  fi
  sleep 2
done

echo "Frontend test failed"
exit 1
