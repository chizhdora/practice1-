from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/territories", tags=["territories"])

@router.get("/", response_model=list[schemas.TerritoryRead])
def read_territories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_territories(db, skip=skip, limit=limit)

@router.get("/{territory_id}", response_model=schemas.TerritoryRead)
def read_territory(territory_id: int, db: Session = Depends(get_db)):
    db_territory = crud.get_territory(db, territory_id)
    if db_territory is None:
        raise HTTPException(status_code=404, detail="Territory not found")
    return db_territory

@router.post("/", response_model=schemas.TerritoryRead, status_code=201)
def create_territory(territory: schemas.TerritoryCreate, db: Session = Depends(get_db)):
    return crud.create_territory(db, territory)

@router.put("/{territory_id}", response_model=schemas.TerritoryRead)
def update_territory(territory_id: int, territory_update: schemas.TerritoryUpdate, db: Session = Depends(get_db)):
    db_territory = crud.update_territory(db, territory_id, territory_update)
    if db_territory is None:
        raise HTTPException(status_code=404, detail="Territory not found")
    return db_territory

@router.delete("/{territory_id}", status_code=204)
def delete_territory(territory_id: int, db: Session = Depends(get_db)):
    if not crud.delete_territory(db, territory_id):
        raise HTTPException(status_code=404, detail="Territory not found")
    return

@router.post("/{territory_id}/metrics", response_model=schemas.MetricRead, status_code=201)
def create_metric(territory_id: int, metric: schemas.MetricCreate, db: Session = Depends(get_db)):
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return crud.create_metric(db, territory_id, metric)

@router.get("/{territory_id}/metrics", response_model=list[schemas.MetricRead])
def read_metrics(territory_id: int, db: Session = Depends(get_db)):
    territory = crud.get_territory(db, territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return crud.get_metrics_by_territory(db, territory_id)