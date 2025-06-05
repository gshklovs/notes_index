# Vite: React + FastAPI + GitHub Actions template for agents 

This project provides a minimal FastAPI backend with a Vite + React frontend. It implemenets a GitHub Actions workflow for running tests on every push and pull request using pytest and vitest. AGENTS.MD is used for improved PRs from OpenAI Codex.

## Requirements
- Python 3.10+
- Node.js 18+

## Setup

All commands should be run from the `frontend` directory.

1.  Clone the repository:
    ```bash
    git clone https://github.com/gshklovs/react-codex-starter.git
    ```

2.  Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

3.  Install frontend dependencies:
    ```bash
    npm install
    ```

4.  Install backend dependencies:
    ```bash
    npm run install:backend
    ```

## Development

Start both frontend and backend servers with a single command:

```bash
cd frontend
npm run dev:all
```

Or run them separately:

**Frontend:**

```bash
cd frontend
npm run dev
```

**Backend:**

```bash
cd backend
uvicorn app.main:app --reload
```

The frontend will be available at http://localhost:5173
The backend API will be available at http://localhost:8000

## Tests
### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm test
```

The backend tests verify the `/api/hello` route. The frontend tests use Vitest and React Testing Library to check component rendering and behavior.


## Continuous Integration

This repository uses GitHub Actions to run tests automatically on every push and pull request. The workflow installs dependencies and executes the same test commands described above.

To run the tests locally:

```bash
pip install -r backend/requirements.txt
npm install --prefix frontend
cd backend && pytest
cd frontend && npm test
```

If any step fails, the workflow marks the commit as failed on GitHub.

## RAG Indexing Feature

This project includes a simple Retrieval-Augmented Generation indexing demo. To
index your own notes:

```
pip install -r backend/requirements.txt
npm install --prefix frontend

# run backend
uvicorn main:app --reload --port 8000 --app-dir backend

# run frontend
npm --prefix frontend run dev
```

Navigate to the "Index Notes" form in the frontend, paste some text, and click
"Index Notes". The backend will split the text into paragraphs and sentences,
generate dummy embeddings, and store them in in-memory FAISS indexes.

Run tests with:

```
cd backend && pytest
cd ../frontend && npm test -- --watch=false
```
