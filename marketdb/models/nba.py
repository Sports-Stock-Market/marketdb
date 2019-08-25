from marketdb.session import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class NBATeam(Base):

    __tablename__ = 'nba_teams'

    id = Column(Integer, primary_key=True)

    team_name = Column(String)
    city = Column(String)
    wins = Column(Integer)
    losses = Column(Integer)
    wins_lastYear = Column(Integer)
    losses_lastYear = Column(Integer)
    conference_standings = Column(Integer)
    playoff_odds = Column(Float)
    starters_rating = Column(Float)
    bench_rating = Column(Float)
    points_for = Column(Int)
    field_goal = Column(Int)
    threePt_made = Column(Int)
    free_throw = Column(Int)
    offensive_rebounds = Column(Int)
    defensive_rebounds = Column(Int)
    assists = Column(Int)
    turnovers = Column(Int)
    plus_minus = Column(Float)
    points_against = Column(Int)
    steals = Column(Int)
    blocks = Column(Int)

    players = relationship("NBAPlayer")

class NBAPlayer(Base):

    __tablename__ = 'nba_players'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('nba_teams.id'))

    first_name = Column(String)
    last_name = Column(String)
    games_played = Column(Int)
    games_started = Column(Int)
    points = Column(Int)
    field_goals_attemped = Column(Int)
    field_goals_made = Column(Int)
    threePt_attempted = Column(Int)
    threePt_made = Column(Int)
    freeThrows_attemped = Column(Int)
    freeThrows_made = Column(Int)
    assists = Column(Int)
    turnovers = Column(Int)
    def_rebounds = Column(Int)
    off_rebounds = Column(Int)
    plus_minus = Column(Float)
    min_per_game = Column(Float)
    win_share = Column(Int)
    true_shooting_pct = Column(Float)
    fouls = Column(Int)
    blocks = Column(Int)
