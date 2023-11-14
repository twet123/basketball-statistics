from pydantic import BaseModel

from . import models, utils


class ShootingStatistics(BaseModel):
    attempts: float = 0
    made: float = 0
    shootingPercentage: float = 0


class TraditionalStatistics(BaseModel):
    freeThrows: ShootingStatistics = ShootingStatistics()
    twoPoints: ShootingStatistics = ShootingStatistics()
    threePoints: ShootingStatistics = ShootingStatistics()
    points: float = 0
    rebounds: float = 0
    blocks: float = 0
    assists: float = 0
    steals: float = 0
    turnovers: float = 0


class AdvancedStatistics(BaseModel):
    valorization: float = 0
    effectiveFieldGoalPercentage: float = 0
    trueShootingPercentage: float = 0
    hollingerAssistRatio: float = 0


class PlayerStats(BaseModel):
    playerName: str
    gamesPlayed: int
    traditional: TraditionalStatistics = TraditionalStatistics()
    advanced: AdvancedStatistics = AdvancedStatistics()

    def add_performance(self, performance: models.Performance) -> None:
        self.traditional.freeThrows.attempts += performance.fta
        self.traditional.freeThrows.made += performance.ftm
        self.traditional.twoPoints.attempts += performance.twopa
        self.traditional.twoPoints.made += performance.twopm
        self.traditional.threePoints.attempts += performance.threepa
        self.traditional.threePoints.made += performance.threepm
        self.traditional.rebounds += performance.reb
        self.traditional.blocks += performance.blk
        self.traditional.assists += performance.ast
        self.traditional.steals += performance.stl
        self.traditional.turnovers += performance.tov

    def calculate_derived(self) -> None:
        self.traditional.freeThrows.shootingPercentage = (
            utils.calculate_shooting_percentage(
                self.traditional.freeThrows.made, self.traditional.freeThrows.attempts
            )
        )
        self.traditional.twoPoints.shootingPercentage = (
            utils.calculate_shooting_percentage(
                self.traditional.twoPoints.made, self.traditional.twoPoints.attempts
            )
        )
        self.traditional.threePoints.shootingPercentage = (
            utils.calculate_shooting_percentage(
                self.traditional.threePoints.made, self.traditional.threePoints.attempts
            )
        )
        self.traditional.points = utils.calculate_points(
            self.traditional.freeThrows.made,
            self.traditional.twoPoints.made,
            self.traditional.threePoints.made,
        )
        self.advanced.valorization = utils.calculate_valorization(
            self.traditional.freeThrows.made,
            self.traditional.twoPoints.made,
            self.traditional.threePoints.made,
            self.traditional.rebounds,
            self.traditional.blocks,
            self.traditional.assists,
            self.traditional.steals,
            self.traditional.freeThrows.attempts,
            self.traditional.twoPoints.attempts,
            self.traditional.threePoints.attempts,
            self.traditional.turnovers,
        )
        self.advanced.effectiveFieldGoalPercentage = (
            utils.calculate_effective_fg_percentage(
                self.traditional.twoPoints.made,
                self.traditional.threePoints.made,
                self.traditional.twoPoints.attempts,
                self.traditional.threePoints.attempts,
            )
        )
        self.advanced.trueShootingPercentage = utils.calculate_true_shooting_percentage(
            self.traditional.points,
            self.traditional.twoPoints.attempts,
            self.traditional.threePoints.attempts,
            self.traditional.freeThrows.attempts,
        )
        self.advanced.hollingerAssistRatio = utils.calculate_hollinger_assist_ratio(
            self.traditional.assists,
            self.traditional.twoPoints.attempts,
            self.traditional.threePoints.attempts,
            self.traditional.freeThrows.attempts,
            self.traditional.turnovers,
        )

    def calculate_averages(self) -> None:
        self.traditional.freeThrows.shootingPercentage = round(
            self.traditional.freeThrows.shootingPercentage, 1
        )
        self.traditional.twoPoints.shootingPercentage = round(
            self.traditional.twoPoints.shootingPercentage, 1
        )
        self.traditional.threePoints.shootingPercentage = round(
            self.traditional.threePoints.shootingPercentage, 1
        )
        self.traditional.freeThrows.attempts = round(
            self.traditional.freeThrows.attempts / self.gamesPlayed, 1
        )
        self.traditional.freeThrows.made = round(
            self.traditional.freeThrows.made / self.gamesPlayed, 1
        )
        self.traditional.twoPoints.attempts = round(
            self.traditional.twoPoints.attempts / self.gamesPlayed, 1
        )
        self.traditional.twoPoints.made = round(
            self.traditional.twoPoints.made / self.gamesPlayed, 1
        )
        self.traditional.threePoints.attempts = round(
            self.traditional.threePoints.attempts / self.gamesPlayed, 1
        )
        self.traditional.threePoints.made = round(
            self.traditional.threePoints.made / self.gamesPlayed, 1
        )
        self.traditional.points = round(self.traditional.points / self.gamesPlayed, 1)
        self.traditional.rebounds = round(
            self.traditional.rebounds / self.gamesPlayed, 1
        )
        self.traditional.blocks = round(self.traditional.blocks / self.gamesPlayed, 1)
        self.traditional.assists = round(self.traditional.assists / self.gamesPlayed, 1)
        self.traditional.steals = round(self.traditional.steals / self.gamesPlayed, 1)
        self.traditional.turnovers = round(
            self.traditional.turnovers / self.gamesPlayed, 1
        )
        self.advanced.valorization = round(
            self.advanced.valorization / self.gamesPlayed, 1
        )
        self.advanced.effectiveFieldGoalPercentage = round(
            self.advanced.effectiveFieldGoalPercentage, 1
        )
        self.advanced.trueShootingPercentage = round(
            self.advanced.trueShootingPercentage, 1
        )
        self.advanced.hollingerAssistRatio = round(
            self.advanced.hollingerAssistRatio, 1
        )

    def prepare_object(self):
        self.calculate_derived()
        self.calculate_averages()
