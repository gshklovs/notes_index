# Contributor Guide

This repository contains a small FastAPI backend and a Vite + React frontend. Keep code clear and concise and prefer the packages already listed in `backend/requirements.txt` and `frontend/package.json`.

## Running the project
See **README.md** for full instructions. In short:

```bash
pip install -r backend/requirements.txt
npm install --prefix frontend
```

The backend tests are run with `pytest` from the `backend` directory. Frontend tests are run with `npm test` from the `frontend` directory (see 'Frontend Testing with Vitest' section below for details).

## Continuous Integration
The workflow in `.github/workflows/ci.yml` mirrors these commands. Pushes and pull requests automatically install the dependencies and execute the tests.

Before submitting a PR:
1. Run the same commands locally and ensure they pass.
2. Keep commit messages and PR descriptions short and informative.

## Frontend Testing with Vitest

Frontend tests are located in the `frontend/src` directory, typically co-located with the components they test (e.g., `App.jsx` and `App.test.jsx`). We use [Vitest](https://vitest.dev/) as the test runner and [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/) for writing tests.

### Running Frontend Tests

To run all frontend tests:

```bash
cd frontend
npm test
```

Vitest will run in watch mode by default. You can press `q` to quit.

### Writing New Tests

1.  **Create a Test File**: For a component like `MyComponent.jsx` in `frontend/src/components/`, create a test file named `MyComponent.test.jsx` in the same directory.
2.  **Write Your Test**:
    *   Import necessary utilities from `vitest` (e.g., `describe`, `it`, `expect`) and `@testing-library/react` (e.g., `render`, `screen`).
    *   Use `describe` to group related tests and `it` for individual test cases.
    *   Render your component using `render()`.
    *   Use `screen` queries (e.g., `screen.getByText()`, `screen.getByRole()`) to find elements.
    *   Use `expect()` with matchers (many from `jest-dom`, available via `frontend/src/setupTests.js`) to make assertions.

    **Example (`frontend/src/App.test.jsx`):**
    ```javascript
    import { render, screen } from '@testing-library/react';
    import App from './App'; // Assuming App.jsx is in the same directory or adjust path
    import { describe, it, expect } from 'vitest';

    describe('App component', () => {
      it('renders Hello World', () => {
        render(<App />);
        const headingElement = screen.getByRole('heading', { name: /Hello World/i });
        expect(headingElement).toBeInTheDocument();
      });

      // Add more test cases for App component here
    });
    ```
3.  **Run Tests**: Execute `npm test` in the `frontend` directory to see your new tests run.

Refer to the Vitest and React Testing Library documentation for more advanced testing scenarios and APIs.


