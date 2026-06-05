from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.sql import func
from .database import Base

class Territory(Base):
    __tablename__ = "territories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    territory_type = Column(String(100), nullable=False)
    level = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class TerritoryMetric(Base):
    __tablename__ = "territory_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    territory_id = Column(Integer, ForeignKey("territories.id", ondelete="CASCADE"), nullable=False)
    year = Column(Integer, nullable=False)
    population = Column(Integer, nullable=True)
    area_km2 = Column(Numeric(12, 2), nullable=True)
    source = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())