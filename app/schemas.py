from pydantic import BaseModel


class ShootingStatistics(BaseModel):
    attempts: float
    made: float
    shootingPercentage: float


class TraditionalStatistics(BaseModel):
    freeThrows: ShootingStatistics
    twoPoints: ShootingStatistics
    threePoints: ShootingStatistics


class AdvancedStatistics(BaseModel):
    valorization: float
    effectiveFieldGoalPercentage: float
    trueShootingPercentage: float
    hollingerAssistRatio: float


class PlayerStats(BaseModel):
    playerName: str
    gamesPlayed: int
    traditional: TraditionalStatistics
    points: float
    rebounds: float
    blocks: float
    assists: float
    steals: float
    turnovers: float
    advanced: AdvancedStatistics
