from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    """Статическая конфигурация приложения (меняется только при перезапуске)."""
    app_name: str = "Laboratory FastAPI App"
    app_version: str = "1.0.0"
    app_description: str = "Учебное приложение для ЛР5"
    app_authors: list = ["Chizhdora"]
    
    class Config:
        env_file = ".env"

class RuntimeConfig:
    """Динамическая конфигурация (меняется через API)."""
    def __init__(self):
        self.log_level = "INFO"
        self.feature_flag = True
        self.maintenance_mode = False
        self.runtime_message = "Приложение работает в штатном режиме"
    
    def update(self, new_config: dict):
        for key, value in new_config.items():
            if hasattr(self, key):
                setattr(self, key, value)
                