# HW-03b External Dependencies Isolation - Mocking

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/endiesworld/codes/tree/HW-03b.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/endiesworld/codes/tree/HW-03b)

## How to run tests

```bash
pytest test/test_fetch_user_repo.py
```

## Continuous Integration

This repository is set up with CircleCI. Every push will trigger a build and run the tests. The badge above shows the current build status for the `HW-03b` branch.

## Project Structure

HW-03b-External-Dependencies-Isolation-Mocking/
├── .python-version
├── pyproject.toml
├── README.md
├── uv.lock
├── src/
│   └── main.py
├── test/
│   └── test_fetch_user_repo.py
└── ... (cache and metadata folders)

**Key folders/files:**

- `src/main.py`: Main application code (GitHub API logic).
- `test/test_fetch_user_repo.py`: Unit tests for the main logic (uses mocking).
- `pyproject.toml`, `requirements.txt`: Project dependencies.

---

## How to Run the Project

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```
