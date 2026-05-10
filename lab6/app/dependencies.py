from fastapi import Request
from .init_dependencies import DependencyContainer
from .schemas.app_config import AppConfigModel
from .services.runtime_config_service import RuntimeConfigService

def get_dependency_container(request: Request) -> DependencyContainer:
    """Возвращает контейнер зависимостей из app.state."""
    return request.app.state.dependencies

def get_app_config(request: Request) -> AppConfigModel:
    """Провайдер для статической конфигурации."""
    container = get_dependency_container(request)
    return container.get_dependency("app_config")

def get_runtime_config_service(request: Request) -> RuntimeConfigService:
    """Провайдер для сервиса runtime-настроек."""
    container = get_dependency_container(request)
    return container.get_dependency("runtime_config_service")
