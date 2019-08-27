from marketdb.session import Base
from sqlalchemy import Column, Text, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship, backref

class NBATeam(Base):

    __tablename__ = 'nba_teams'

    id = Column(Integer, primary_key=True)

    team_name = Column(Text)
    city = Column(Text)
    wins = Column(Integer)
    losses = Column(Integer)
    wins_lastYear = Column(Integer)
    losses_lastYear = Column(Integer)
    conference_standings = Column(Integer)
    playoff_odds = Column(Float)
    starters_rating = Column(Float)
    bench_rating = Column(Float)
    points_for = Column(Integer)
    field_goal = Column(Integer)
    threePt_made = Column(Integer)
    free_throw = Column(Integer)
    offensive_rebounds = Column(Integer)
    defensive_rebounds = Column(Integer)
    assists = Column(Integer)
    turnovers = Column(Integer)
    plus_minus = Column(Float)
    points_against = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)

    players = relationship("NBAPlayer")

    def __init__(self, city, team_name, wins, losses, wins_lastYear,
                 losses_lastYear, conference_standings, playoff_odds,
                 starters_rating, bench_rating, points_for, field_goal,
                 threePt_made, free_throw, offensive_rebounds,
                 defensive_rebounds, assists, turnovers, plus_minus,
                 points_against, steals, blocks):
        self.team_name = team_name
        self.city = city
        self.wins = wins
        self.losses = losses
        self.wins_lastYear = wins_lastYear
        self.losses_lastYear = losses_lastYear
        self.conference_standings = conference_standings
        self.playoff_odds = playoff_odds
        self.starters_rating = starters_rating
        self.bench_rating = bench_rating
        self.points_for = points_for
        self.field_goal = field_goal
        self.threePt_made = threePt_made
        self.free_throw = free_throw
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.assists = assists
        self.turnovers = turnovers
        self.plus_minus = plus_minus
        self.points_against = points_against
        self.steals = steals
        self.blocks = blocks

    def __str__(self):
        return f'Team: \'{self.city} {self.team_name}\', ID: {self.id}'

class NBAPlayer(Base):

    __tablename__ = 'nba_players'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('nba_teams.id'))
    team = relationship("NBATeam")

    first_name = Column(Text)
    last_name = Column(Text)
    games_played = Column(Integer)
    games_started = Column(Integer)
    points = Column(Integer)
    field_goals_attempted = Column(Integer)
    field_goals_made = Column(Integer)
    threePt_attempted = Column(Integer)
    threePt_made = Column(Integer)
    freeThrows_attempted = Column(Integer)
    freeThrows_made = Column(Integer)
    assists = Column(Integer)
    turnovers = Column(Integer)
    def_rebounds = Column(Integer)
    off_rebounds = Column(Integer)
    plus_minus = Column(Float)
    min_per_game = Column(Float)
    win_share = Column(Integer)
    true_shooting_pct = Column(Float)
    fouls = Column(Integer)
    blocks = Column(Integer)

    def __init__(self, first_name, last_name, games_played, games_started,
                 points, field_goals_attempted, field_goals_made,
                 threePt_attempted, threePt_made, freeThrows_attempted,
                 freeThrows_made, assists, turnovers, defensive_rebounds,
                 offensive_rebounds, plus_minus, min_per_game, win_share,
                 true_shooting_pct, fouls, blocks, team):
        if team == None:
            raise ValueError('\'team\' field cannot be left as None.')

        self.first_name = first_name
        self.last_name = last_name
        self.games_played = games_played
        self.games_started = games_started
        self.points = points
        self.field_goals_attempted = field_goals_attempted
        self.field_goals_made = field_goals_made
        self.threePt_attempted = threePt_attempted
        self.threePt_made = threePt_made
        self.freeThrows_attempted = freeThrows_attempted
        self.freeThrows_made = freeThrows_made
        self.assists = assists
        self.turnovers = turnovers
        self.defensive_rebounds = defensive_rebounds
        self.offensive_rebounds = offensive_rebounds
        self.plus_minus = plus_minus
        self.min_per_game = min_per_game
        self.win_share = win_share
        self.true_shooting_pct = true_shooting_pct
        self.fouls = fouls
        self.blocks = blocks
        self.team = team

    def __str__(self):
        return f'Player: {self.first_name} {self.last_name}, ID: {self.id}'
