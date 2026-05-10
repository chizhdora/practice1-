from pydantic import BaseModel, Field
from typing import Literal

class RuntimeConfigModel(BaseModel):
    """Модель для хранения runtime-настроек."""
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(default="INFO")
    feature_flag: bool = Field(default=True)
    maintenance_mode: bool = Field(default=False)
    runtime_message: str = Field(default="Приложение работает в штатном режиме")

class RuntimeConfigUpdateModel(BaseModel):
    """Модель для обновления runtime-настроек через API."""
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]
    feature_flag: bool
    maintenance_mode: bool
    runtime_message: str
    