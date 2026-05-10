from pydantic import BaseModel, Field
from typing import List

class AppConfigModel(BaseModel):
    """Статическая конфигурация приложения (меняется только при перезапуске)."""
    app_name: str = Field(default="Laboratory FastAPI App")
    app_version: str = Field(default="1.0.0")
    app_description: str = Field(default="Учебное приложение на FastAPI")
    app_authors: List[str] = Field(default=["Chizhdora"])