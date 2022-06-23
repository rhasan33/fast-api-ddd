from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get(
    path="/",
    status_code=200,
    description="Healthcheck endpoint for the auth service",
    tags=["utility"],
)
async def health_check() -> Dict:
    return {"status": "ok"}
