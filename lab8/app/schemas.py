from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TerritoryBase(BaseModel):
    name: str
    territory_type: str
    level: int

class TerritoryCreate(TerritoryBase):
    pass

class TerritoryUpdate(BaseModel):
    name: Optional[str] = None
    territory_type: Optional[str] = None
    level: Optional[int] = None

class TerritoryRead(TerritoryBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class MetricBase(BaseModel):
    year: int
    population: Optional[int] = None
    area_km2: Optional[float] = None
    source: Optional[str] = None

class MetricCreate(MetricBase):
    pass

class MetricRead(MetricBase):
    id: int
    territory_id: int
    created_at: datetime

    class Config:
        from_attributes = True