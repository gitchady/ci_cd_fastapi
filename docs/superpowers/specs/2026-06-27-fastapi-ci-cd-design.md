# FastAPI CI/CD учебный пример

## Цель

Сделать маленький проект на Python FastAPI, который показывает базовую цепочку CI/CD:

- приложение запускается локально через `uvicorn`;
- есть простые API-эндпоинты;
- тесты проверяют поведение API;
- GitHub Actions запускает CI;
- Dockerfile показывает упаковку приложения;
- учебный CD job имитирует деплой после успешного CI.

## Архитектура

Проект состоит из:

- `app/main.py` - FastAPI приложение;
- `tests/test_main.py` - тесты через FastAPI `TestClient`;
- `requirements.txt` - зависимости приложения и тестов;
- `Dockerfile` - сборка контейнера;
- `.github/workflows/ci-cd.yml` - pipeline CI/CD;
- `README.md` - команды запуска и объяснение pipeline.

## API

Эндпоинты:

- `GET /` возвращает приветствие;
- `GET /health` возвращает статус сервиса;
- `GET /items/{item_id}` возвращает простой учебный объект.

## CI/CD

CI job:

- ставит Python;
- устанавливает зависимости;
- запускает `pytest`;
- собирает Docker image.

CD job:

- зависит от CI;
- запускается только для ветки `main`;
- имитирует деплой командой `echo`, чтобы пример был безопасным и не требовал сервера.

## Проверка

Готовность подтверждается успешным запуском:

- `python -m pytest`;
- опционально `uvicorn app.main:app --reload`;
- опционально `docker build -t fastapi-ci-cd-demo .`.
