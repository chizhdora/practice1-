from fastapi import FastAPI
from config import AppConfig, RuntimeConfig

# Загружаем статическую конфигурацию (только при запуске)
app_config = AppConfig()

# Создаём приложение FastAPI со статическими настройками
app = FastAPI(
    title=app_config.app_name,
    version=app_config.app_version,
    description=app_config.app_description
)

# Создаём глобальный объект для runtime-настроек
runtime_config = RuntimeConfig()

@app.get("/health")
async def health_check():
    """Проверка работоспособности приложения."""
    return {"status": "ok"}

@app.get("/config/app")
async def get_static_config():
    """Возвращает статическую конфигурацию."""
    return {
        "app_name": app_config.app_name,
        "app_version": app_config.app_version,
        "app_description": app_config.app_description,
        "app_authors": app_config.app_authors
    }

@app.get("/config/runtime")
async def get_runtime_config():
    """Возвращает текущие runtime-настройки."""
    return {
        "log_level": runtime_config.log_level,
        "feature_flag": runtime_config.feature_flag,
        "maintenance_mode": runtime_config.maintenance_mode,
        "runtime_message": runtime_config.runtime_message
    }

@app.put("/config/runtime")
async def update_runtime_config(new_config: dict):
    """Обновляет runtime-настройки."""
    runtime_config.update(new_config)
    return {"message": "Runtime config updated successfully", "new_config": new_config}
