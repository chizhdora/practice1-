from sqlalchemy.orm import Session
from . import models, schemas

def get_territory(db: Session, territory_id: int):
    return db.query(models.Territory).filter(models.Territory.id == territory_id).first()

def get_territories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Territory).offset(skip).limit(limit).all()

def create_territory(db: Session, territory: schemas.TerritoryCreate):
    db_territory = models.Territory(
        name=territory.name,
        territory_type=territory.territory_type,
        level=territory.level
    )
    db.add(db_territory)
    db.commit()
    db.refresh(db_territory)
    return db_territory

def update_territory(db: Session, territory_id: int, territory_update: schemas.TerritoryUpdate):
    db_territory = get_territory(db, territory_id)
    if not db_territory:
        return None
    update_data = territory_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_territory, key, value)
    db.commit()
    db.refresh(db_territory)
    return db_territory

def delete_territory(db: Session, territory_id: int):
    db_territory = get_territory(db, territory_id)
    if not db_territory:
        return False
    db.delete(db_territory)
    db.commit()
    return True

def create_metric(db: Session, territory_id: int, metric: schemas.MetricCreate):
    db_metric = models.TerritoryMetric(territory_id=territory_id, **metric.model_dump())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

def get_metrics_by_territory(db: Session, territory_id: int):
    return db.query(models.TerritoryMetric).filter(models.TerritoryMetric.territory_id == territory_id).all()