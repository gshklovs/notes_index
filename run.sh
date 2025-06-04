#!/usr/bin/env bash
set -euo pipefail

BACKEND_PORT=8000
FRONTEND_PORT=3000

pushd backend >/dev/null
pip install -r requirements.txt
uvicorn main:app --reload --port $BACKEND_PORT &
BACK_PID=$!
popd >/dev/null

pushd frontend >/dev/null
npm install
npm run dev -- --port $FRONTEND_PORT &
FRONT_PID=$!
popd >/dev/null

trap "kill $BACK_PID $FRONT_PID" EXIT

echo "Backend running on http://localhost:$BACKEND_PORT"
echo "Frontend running on http://localhost:$FRONTEND_PORT"
echo "Press Ctrl+C to stop."

wait
