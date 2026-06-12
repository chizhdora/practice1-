from fastapi import FastAPI
from .routers import territories
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Urban Spatial API (CRUD)", version="1.0.0")

app.include_router(territories.router)

@app.get("/health")
def health():
    return {"status": "ok"}