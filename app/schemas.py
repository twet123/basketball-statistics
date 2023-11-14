from pydantic import BaseModel

from . import models


class ShootingStatistics(BaseModel):
    attempts: float
    made: float
    shootingPercentage: float


class TraditionalStatistics(BaseModel):
    freeThrows: ShootingStatistics
    twoPoints: ShootingStatistics
    threePoints: ShootingStatistics
    points: float
    rebounds: float
    blocks: float
    assists: float
    steals: float
    turnovers: float


class AdvancedStatistics(BaseModel):
    valorization: float
    effectiveFieldGoalPercentage: float
    trueShootingPercentage: float
    hollingerAssistRatio: float


class PlayerStats(BaseModel):
    playerName: str
    gamesPlayed: int
    traditional: TraditionalStatistics
    advanced: AdvancedStatistics

    def add_performance(self, performance: models.Performance) -> None:
        self.traditional.freeThrows.attempts += performance.fta
        self.traditional.freeThrows.made += performance.ftm
        self.traditional.freeThrows.shootingPercentage += (
            performance.get_free_thow_percentage()
        )
        self.traditional.twoPoints.attempts += performance.twopa
        self.traditional.twoPoints.made += performance.twopm
        self.traditional.twoPoints.shootingPercentage += (
            performance.get_two_point_percentage()
        )
        self.traditional.threePoints.attempts += performance.threepa
        self.traditional.threePoints.made += performance.threepm
        self.traditional.threePoints.shootingPercentage += (
            performance.get_three_point_percentage()
        )
        self.traditional.points += performance.get_points()
        self.traditional.rebounds += performance.reb
        self.traditional.blocks += performance.blk
        self.traditional.assists += performance.ast
        self.traditional.steals += performance.stl
        self.traditional.turnovers += performance.tov
        self.advanced.valorization += performance.get_valorization()
        self.advanced.effectiveFieldGoalPercentage += (
            performance.get_effective_fg_percentage()
        )
        self.advanced.trueShootingPercentage += (
            performance.get_true_shooting_percentage()
        )
        self.advanced.hollingerAssistRatio += performance.get_hollinger_assist_ratio()

    def calculate_averages(self) -> None:
        self.traditional.freeThrows.attempts /= self.gamesPlayed
        self.traditional.freeThrows.made /= self.gamesPlayed
        self.traditional.freeThrows.shootingPercentage /= self.gamesPlayed
        self.traditional.twoPoints.attempts /= self.gamesPlayed
        self.traditional.twoPoints.made /= self.gamesPlayed
        self.traditional.twoPoints.shootingPercentage /= self.gamesPlayed
        self.traditional.threePoints.attempts /= self.gamesPlayed
        self.traditional.threePoints.made /= self.gamesPlayed
        self.traditional.threePoints.shootingPercentage /= self.gamesPlayed
        self.traditional.points /= self.gamesPlayed
        self.traditional.rebounds /= self.gamesPlayed
        self.traditional.blocks /= self.gamesPlayed
        self.traditional.assists /= self.gamesPlayed
        self.traditional.steals /= self.gamesPlayed
        self.traditional.turnovers /= self.gamesPlayed
        self.advanced.valorization /= self.gamesPlayed
        self.advanced.effectiveFieldGoalPercentage /= self.gamesPlayed
        self.advanced.trueShootingPercentage /= self.gamesPlayed
        self.advanced.hollingerAssistRatio /= self.gamesPlayed
