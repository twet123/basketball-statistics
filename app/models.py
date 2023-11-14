from sqlalchemy import Column, String, Integer, Double
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

    def __init__(
        self,
        id: int,
        player: str,
        position: str,
        ftm: int,
        fta: int,
        twopm: int,
        twopa: int,
        threepm: int,
        threepa: int,
        reb: int,
        blk: int,
        ast: int,
        stl: int,
        tov: int,
    ) -> None:
        self.id = id
        self.player = player
        self.position = position
        self.ftm = ftm
        self.fta = fta
        self.twopm = twopm
        self.twopa = twopa
        self.threepm = threepm
        self.threepa = threepa
        self.reb = reb
        self.blk = blk
        self.ast = ast
        self.stl = stl
        self.tov = tov
