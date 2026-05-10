from pydantic import BaseModel
from typing import Literal, Dict, Any

class HealthResponse(BaseModel):
    """Ответ для эндпоинта /health."""
    status: Literal["ok"] = "ok"

class AppConfigResponse(BaseModel):
    """Ответ для GET /config/app."""
    app_name: str
    app_version: str
    app_description: str
    app_authors: list[str]

class RuntimeConfigResponse(BaseModel):
    """Ответ для GET /config/runtime и PUT /config/runtime."""
    log_level: str
    feature_flag: bool
    maintenance_mode: bool
    runtime_message: str