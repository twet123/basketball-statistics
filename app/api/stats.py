from fastapi import APIRouter

router = APIRouter()


@router.get("/stats/player/{player_full_name}")
def get_player_statistics(player_full_name: str):
    return {"player_full_name": player_full_name}
