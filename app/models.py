from sqlalchemy import Column, String, Integer
from .database import Base


class Performance(Base):
    __tablename__ = "performances"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    player = Column("player", String)
    position = Column("position", String)
    ftm = Column("ftm", Integer)
    fta = Column("fta", Integer)
    twopm = Column("twopm", Integer)
    twopa = Column("twopa", Integer)
    threepm = Column("threepm", Integer)
    threepa = Column("threepa", Integer)
    reb = Column("reb", Integer)
    blk = Column("blk", Integer)
    ast = Column("ast", Integer)
    stl = Column("stl", Integer)
    tov = Column("tov", Integer)

    def __init__(self, performance: dict[str, str]) -> None:
        self.player = performance["PLAYER"]
        self.position = performance["POSITION"]
        self.ftm = int(performance["FTM"])
        self.fta = int(performance["FTA"])
        self.twopm = int(performance["2PM"])
        self.twopa = int(performance["2PA"])
        self.threepm = int(performance["3PM"])
        self.threepa = int(performance["3PA"])
        self.reb = int(performance["REB"])
        self.blk = int(performance["BLK"])
        self.ast = int(performance["AST"])
        self.stl = int(performance["STL"])
        self.tov = int(performance["TOV"])

    def get_free_thow_percentage(self) -> float:
        return self.ftm / self.fta * 100

    def get_two_point_percentage(self) -> float:
        return self.twopm / self.twopa * 100

    def get_three_point_percentage(self) -> float:
        return self.threepm / self.threepa * 100

    def get_points(self) -> int:
        return self.ftm + 2 * self.twopm + 3 * self.threepm

    def get_valorization(self) -> int:
        return (self.get_points() + self.reb + self.blk + self.ast + self.stl) - (
            self.fta
            - self.ftm
            + self.twopa
            - self.twopm
            + self.threepa
            - self.threepm
            + self.tov
        )

    def get_effective_fg_percentage(self) -> float:
        return (
            (self.towpm + self.threepm + 0.5 * self.threepm)
            / (self.twopa + self.threepa)
            * 100
        )

    def get_true_shooting_percentage(self) -> float:
        return (
            self.get_points()
            / (2 * (self.twopa + self.threepa + 0.475 * self.fta))
            * 100
        )

    def get_hollinger_assist_ratio(self) -> float:
        return (
            self.ast
            / (self.twopa + self.threepa + 0.475 * self.fta + self.ast + self.tov)
            * 100
        )
