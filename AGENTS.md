# Contributor Guide

This repository contains a small FastAPI backend and a Vite + React frontend. Keep code clear and concise and prefer the packages already listed in `backend/requirements.txt` and `frontend/package.json`.

## Running the project
See **README.md** for full instructions. In short:

```bash
pip install -r backend/requirements.txt
npm install --prefix frontend
```

The backend tests are run with `pytest` from the project root and the frontend test script is `./frontend/tests/test_frontend.sh`.

## Continuous Integration
The workflow in `.github/workflows/ci.yml` mirrors these commands. Pushes and pull requests automatically install the dependencies and execute the tests.

Before submitting a PR:
1. Run the same commands locally and ensure they pass.
2. Keep commit messages and PR descriptions short and informative.


