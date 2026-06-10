from fastapi import APIRouter, Depends
from ..schemas.responses import HealthResponse, AppConfigResponse, RuntimeConfigResponse
from ..schemas.runtime_config import RuntimeConfigUpdateModel
from ..schemas.app_config import AppConfigModel
from ..services.runtime_config_service import RuntimeConfigService
from ..dependencies import get_app_config, get_runtime_config_service

router = APIRouter(tags=["configuration"])

@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Проверка работоспособности приложения."""
    return HealthResponse(status="ok")

@router.get("/config/app", response_model=AppConfigResponse)
def get_static_config(app_config: AppConfigModel = Depends(get_app_config)) -> AppConfigResponse:
    """Возвращает статическую конфигурацию."""
    return AppConfigResponse(
        app_name=app_config.app_name,
        app_version=app_config.app_version,
        app_description=app_config.app_description,
        app_authors=app_config.app_authors
    )

@router.get("/config/runtime", response_model=RuntimeConfigResponse)
def get_runtime_config(service: RuntimeConfigService = Depends(get_runtime_config_service)) -> RuntimeConfigResponse:
    """Возвращает текущие runtime-настройки."""
    config = service.get_config()
    return RuntimeConfigResponse(
        log_level=config.log_level,
        feature_flag=config.feature_flag,
        maintenance_mode=config.maintenance_mode,
        runtime_message=config.runtime_message
    )

@router.put("/config/runtime", response_model=RuntimeConfigResponse)
def update_runtime_config(
    new_config: RuntimeConfigUpdateModel,
    service: RuntimeConfigService = Depends(get_runtime_config_service)
) -> RuntimeConfigResponse:
    """Обновляет runtime-настройки."""
    updated = service.update_config(new_config)
    return RuntimeConfigResponse(
        log_level=updated.log_level,
        feature_flag=updated.feature_flag,
        maintenance_mode=updated.maintenance_mode,
        runtime_message=updated.runtime_message
    )
    