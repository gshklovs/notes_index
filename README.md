# notes_index Hello World Template

This project provides a minimal FastAPI backend with a Vite + React frontend. It demonstrates end‑to‑end functionality with automated tests.

## Requirements
- Python 3.10+
- Node.js 18+

## Setup
Install backend and frontend dependencies:

```bash
cd backend && pip install -r requirements.txt
cd ../frontend && npm install
```

## Running the app
Use the helper script to start both servers:

```bash
./run.sh
```

The frontend will be available on `http://localhost:3000` and will fetch data from the backend endpoint `http://localhost:8000/api/hello`.

## Tests
### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
./tests/test_frontend.sh
```

The backend tests verify the `/api/hello` route. The frontend test starts the Vite dev server and checks that the page contains "Hello World".

