from typing import Dict, Any
from .schemas.app_config import AppConfigModel
from .schemas.runtime_config import RuntimeConfigModel
from .services.runtime_config_service import RuntimeConfigService

class DependencyContainer(Dict[str, Any]):
    """Кастомный словарь зависимостей с безопасным получением."""
    
    def get_dependency(self, key: str):
        if key not in self:
            raise KeyError(f"Зависимость '{key}' не найдена в контейнере")
        return self[key]

def init_dependencies() -> DependencyContainer:
    """Инициализирует все зависимости приложения."""
    container = DependencyContainer()
    
    # Статическая конфигурация
    app_config = AppConfigModel()
    container["app_config"] = app_config
    
    # Runtime-сервис (с начальной конфигурацией)
    initial_runtime = RuntimeConfigModel()
    runtime_service = RuntimeConfigService(initial_runtime)
    container["runtime_config_service"] = runtime_service
    
    return container
