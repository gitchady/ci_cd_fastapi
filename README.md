# FastAPI CI/CD Demo

Учебный пример простого CI/CD для Python FastAPI.

## Что внутри

- `app/main.py` - маленькое FastAPI API.
- `tests/test_main.py` - тесты API.
- `Dockerfile` - сборка Docker image.
- `.github/workflows/ci-cd.yml` - GitHub Actions pipeline.

## Локальный запуск

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Открыть:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/health

## Тесты

```powershell
python -m pytest -q
```

## Docker

```powershell
docker build -t fastapi-ci-cd-demo .
docker run --rm -p 8000:8000 fastapi-ci-cd-demo
```

## Как работает CI/CD

Pipeline находится в `.github/workflows/ci-cd.yml`.

При `push` или `pull_request` в ветку `main`:

1. GitHub Actions забирает код.
2. Ставит Python 3.12.
3. Устанавливает зависимости.
4. Запускает тесты.
5. Собирает Docker image.

После успешного CI на `push` в `main` запускается учебный CD job:

```text
Deploying fastapi-ci-cd-demo to staging...
```

Это имитация деплоя, чтобы пример был безопасным и не требовал сервера.
