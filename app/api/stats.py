from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from .. import deps, models

router = APIRouter()


@router.get("/stats/player/{player_full_name}")
def get_player_statistics(player_full_name: str):
    return {"player_full_name": player_full_name}


@router.get("/stats")
def get_all_peformances(db: Session = Depends(deps.get_db)):
    return db.query(models.Performance).all()
