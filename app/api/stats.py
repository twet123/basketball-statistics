from sqlalchemy.orm import Session, Query
from fastapi import APIRouter, Depends, HTTPException

from .. import deps, models, schemas

router = APIRouter()


@router.get("/stats/player/{player_full_name}", response_model=schemas.PlayerStats)
def get_player_statistics(player_full_name: str, db: Session = Depends(deps.get_db)):
    query: Query[models.Performance] = db.query(models.Performance).filter(
        models.Performance.player == player_full_name
    )
    count: int = query.count()

    if count == 0:
        raise HTTPException(404, "Player not found")

    response = schemas.PlayerStats(playerName=player_full_name, gamesPlayed=count)
    for performance in query.yield_per(1000):
        response.add_performance(performance)
    response.prepare_object()

    return response


@router.get("/stats")
def get_all(db: Session = Depends(deps.get_db)):
    return db.query(models.Performance).all()
