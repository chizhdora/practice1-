from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .init_dependencies import init_dependencies
from .routes.config import router as config_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Жизненный цикл приложения: инициализация зависимостей при старте."""
    print(" Initializing dependencies...")
    dependencies = init_dependencies()
    app.state.dependencies = dependencies
    print(" Dependencies initialized:", list(dependencies.keys()))
    yield
    print(" App is shutting down...")

app = FastAPI(
    lifespan=lifespan,
    title="Laboratory FastAPI App",
    description="Учебное приложение с Pydantic-моделями и DI",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Перенаправляет на Swagger UI."""
    return RedirectResponse(url="/docs")

app.include_router(config_router) 