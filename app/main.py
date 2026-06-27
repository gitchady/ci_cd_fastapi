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
