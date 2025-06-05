# notes_index Hello World Template

This project provides a minimal FastAPI backend with a Vite + React frontend. It demonstrates end‑to‑end functionality with automated tests.

## Requirements
- Python 3.10+
- Node.js 18+

## Setup

All commands should be run from the `frontend` directory.

1.  Navigate to the frontend directory:
    ```bash
    cd frontend
    ```
2.  Install frontend dependencies:
    ```bash
    npm install
    ```
3.  Install backend dependencies:
    ```bash
    npm run install:backend
    ```

## Running the Application

You will need two separate terminal windows to run both the backend and frontend services. All commands should be run from the `frontend` directory.

1.  **Navigate to the frontend directory** (if not already there):
    ```bash
    cd frontend
    ```

2.  **Start the Backend Service:**
    Open your first terminal, navigate to the `frontend` directory (if you aren't already there from the setup step), and run:
    ```bash
    npm run start:backend
    ```
    The backend API will be available at `http://localhost:8000`.

3.  **Start the Frontend Service:**
    Open your second terminal, navigate to the `frontend` directory (if you aren't already there from the setup step), and run:
    ```bash
    npm run start:frontend
    ```
    The frontend application will be available at `http://localhost:3000`. It is configured to fetch data from the backend at `http://localhost:8000/api/hello`.

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


## Continuous Integration

This repository uses GitHub Actions to run tests automatically on every push and pull request. The workflow installs dependencies and executes the same test commands described above.

To run the tests locally:

```bash
pip install -r backend/requirements.txt
npm install --prefix frontend
cd backend && pytest
cd frontend && ./tests/test_frontend.sh
```

If any step fails, the workflow marks the commit as failed on GitHub.
