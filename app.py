from fastapi import FastAPI
from router import table
from settings import Settings

APP_NAME = "postgres-manager-api"

app = FastAPI(title="Postgres Manager API", description="API for postgres management")
app.include_router(table.router)

settings = Settings()

# TODO Add Prometheus


@app.get("/")
def root():
    return {"status": "ok"}
