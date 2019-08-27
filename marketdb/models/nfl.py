from marketdb.session import Base
from sqlalchemy import Column, Text, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, backref

class NFLTeam(Base):

    __tablename__ = 'nfl_teams'

    id = Column(Integer, primary_key=True)

    city = Column(Text)
    team_name = Column(Text)
    wins = Column(Integer)
    losses = Column(Integer)
    ties = Column(Integer)
    wins_lastYear = Column(Integer)
    losses_lastYear = Column(Integer)
    ties_lastYear = Column(Integer)
    playoff_odds = Column(Float)
    team_rating = Column(Float)
    offense_rating = Column(Float)
    qb_rating = Column(Float)
    offensive_pointsFor = Column(Integer)
    yards_for = Column(Integer)
    touchdowns_for = Column(Integer)
    offensive_redzone_eff = Column(Float)
    defense_rating = Column(Float)
    yards_against = Column(Integer)
    points_against = Column(Integer)
    touchdowns_against = Column(Integer)
    sacks = Column(Integer)
    interceptions = Column(Integer)
    defensive_redzone_eff = Column(Integer)
    defensive_pointsFor = Column(Integer)
    defensive_eff = Column(Float)

    players = relationship("NFLPlayer")

    def __init__(self, city, name, wins, losses, ties, wins_lastYear, losses_lastYear,
                 ties_lastYear, playoff_odds, team_rating, offense_rating,
                 qb_rating, offensive_pointsFor, yards_for, touchdowns_for,
                 offensive_redzone_eff, defense_rating, yards_against, points_against,
                 touchdowns_against, sacks, interceptions, defensive_redzone_eff,
                 defensive_pointsFor, defensive_eff):
        self.city = city
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.wins_lastYear = wins_lastYear
        self.losses_lastYear = losses_lastYear
        self.ties_lastYear = ties_lastYear
        self.playoff_odds = playoff_odds
        self.team_rating = team_rating
        self.offense_rating = offense_rating
        self.qb_rating = qb_rating
        self.offensive_pointsFor = offensive_pointsFor
        self.yards_for = yards_for
        self.touchdowns_for = touchdowns_for
        self.offensive_redzone_eff = offensive_redzone_eff
        self.defense_rating = defense_rating
        self.yards_against = yards_against
        self.points_against = points_against
        self.touchdowns_against = touchdowns_against
        self.sacks = sacks
        self.interceptions = interceptions
        self.defensive_redzone_eff = defensive_redzone_eff
        self.defensive_pointsFor = defensive_pointsFor
        self.defensive_eff = defensive_eff

    def __str__(self):
        return f'{self.city} {self.name}' 
