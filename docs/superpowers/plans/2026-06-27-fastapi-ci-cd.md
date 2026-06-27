# FastAPI CI/CD Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a small FastAPI project that demonstrates a basic CI/CD pipeline for learning.

**Architecture:** The app is a simple API in `app/main.py` with tests in `tests/test_main.py`. CI installs dependencies, runs tests, and builds a Docker image; CD is a safe simulated deploy job.

**Tech Stack:** Python, FastAPI, pytest, uvicorn, Docker, GitHub Actions.

---

## File Structure

- `app/__init__.py` - marks the app package.
- `app/main.py` - FastAPI application and routes.
- `tests/test_main.py` - API tests through `TestClient`.
- `requirements.txt` - runtime and test dependencies.
- `Dockerfile` - container image definition.
- `.dockerignore` - files excluded from Docker context.
- `.github/workflows/ci-cd.yml` - CI/CD workflow.
- `README.md` - learning notes and commands.

### Task 1: FastAPI App

**Files:**
- Create: `app/__init__.py`
- Create: `app/main.py`
- Create: `requirements.txt`

- [ ] **Step 1: Add dependencies**

Create `requirements.txt`:

```txt
fastapi==0.115.6
uvicorn[standard]==0.34.0
pytest==8.3.4
httpx==0.28.1
```

- [ ] **Step 2: Add FastAPI app**

Create `app/main.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="FastAPI CI/CD Demo")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI CI/CD demo"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, int | str]:
    return {"item_id": item_id, "name": f"Item {item_id}"}
```

### Task 2: Tests

**Files:**
- Create: `tests/test_main.py`

- [ ] **Step 1: Add API tests**

Create `tests/test_main.py`:

```python
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_returns_message() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI CI/CD demo"}


def test_health_check_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_read_item_returns_item() -> None:
    response = client.get("/items/42")

    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "name": "Item 42"}
```

- [ ] **Step 2: Run tests**

Run: `python -m pytest -q`
Expected: all tests pass.

### Task 3: Docker

**Files:**
- Create: `Dockerfile`
- Create: `.dockerignore`

- [ ] **Step 1: Add Dockerfile**

Create `Dockerfile`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

- [ ] **Step 2: Add Docker ignore file**

Create `.dockerignore`:

```gitignore
.git
.github
.pytest_cache
__pycache__
*.pyc
.venv
venv
docs
tests
```

- [ ] **Step 3: Build image**

Run: `docker build -t fastapi-ci-cd-demo .`
Expected: image builds successfully when Docker is available.

### Task 4: GitHub Actions CI/CD

**Files:**
- Create: `.github/workflows/ci-cd.yml`

- [ ] **Step 1: Add workflow**

Create `.github/workflows/ci-cd.yml`:

```yaml
name: CI/CD

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

jobs:
  ci:
    name: Test and build
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: python -m pytest -q

      - name: Build Docker image
        run: docker build -t fastapi-ci-cd-demo .

  deploy-staging:
    name: Deploy to staging
    runs-on: ubuntu-latest
    needs: ci
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'

    steps:
      - name: Simulate deploy
        run: echo "Deploying fastapi-ci-cd-demo to staging..."
```

### Task 5: README

**Files:**
- Create: `README.md`

- [ ] **Step 1: Add usage docs**

Create `README.md` with local run, test, Docker, and CI/CD explanation.

- [ ] **Step 2: Verify project**

Run: `python -m pytest -q`
Expected: all tests pass.
