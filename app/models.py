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
