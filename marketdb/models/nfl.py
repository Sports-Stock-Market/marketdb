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

    players = relationship('NFLPlayer')

    def __init__(self, city, team_name, wins, losses, ties, wins_lastYear, losses_lastYear,
                 ties_lastYear, playoff_odds, team_rating, offense_rating,
                 qb_rating, offensive_pointsFor, yards_for, touchdowns_for,
                 offensive_redzone_eff, defense_rating, yards_against, points_against,
                 touchdowns_against, sacks, interceptions, defensive_redzone_eff,
                 defensive_pointsFor, defensive_eff):
        self.city = city
        self.team_name = team_name
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

class NFLPlayer(Base):

    __tablename__ = 'nfl_players'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('nfl_teams.id'))
    team = relationship('NFLTeam')
    
    position = Column(Integer)
    first_name = Column(Text)
    last_name = Column(Text)
    games_played = Column(Integer)
    games_started = Column(Integer)
    passing_completions = Column(Integer)
    pass_attempts = Column(Integer)
    passing_yards = Column(Integer)
    passing_touchdowns = Column(Integer)
    interceptions_against = Column(Integer)
    sacks_against = Column(Integer)
    fumbles_against = Column(Integer)
    qbr = Column(Float)
    rushing_attempts = Column(Integer)
    rushing_yards = Column(Integer)
    rushing_touchdowns = Column(Integer)
    receiving_targets = Column(Integer)
    receptions = Column(Integer)
    receiving_yards = Column(Integer)
    receiving_touchdowns = Column(Integer)
    interceptions_for = Column(Integer)
    pick_sixes = Column(Integer)
    forced_fumbles_for = Column(Integer)
    fumble_recovery_for = Column(Integer)
    fumble_sixes = Column(Integer)
    passes_defended = Column(Integer)
    sacks_for = Column(Integer)
    total_tackles = Column(Integer)
    solo_tackles = Column(Integer)
    tackles_for_loss = Column(Integer)
    qb_hits = Column(Integer)
    fg_attempted = Column(Integer)
    fg_made = Column(Integer)
    longfg_attempted = Column(Integer)
    longfg_made = Column(Integer)
    xp_attempted = Column(Integer)
    xp_made = Column(Integer)
    punt_attempts = Column(Integer)
    punt_yards = Column(Integer)
    punt_returns = Column(Integer)
    punt_return_yards = Column(Integer)
    punt_return_touchdowns = Column(Integer)
    kick_returns = Column(Integer)
    kick_return_yards = Column(Integer)
    kick_return_touchdowns = Column(Integer)

    def __init__(self, position, first_name, last_name, games_played, games_started,
                 passing_completions, pass_attempts, passing_yards, passing_touchdowns,
                 interceptions_against, sacks_against, fumbles_against, qbr,
                 rushing_attempts, rushing_yards, rushing_touchdowns, receiving_targets,
                 receptions, receiving_yards, receiving_touchdowns, interceptions_for,
                 pick_sixes, forced_fumbles_for, fumble_recovery_for, fumble_sixes,
                 passes_defended, sacks_for, total_tackles, solo_tackles, tackles_for_loss,
                 qb_hits, fg_attempted, fg_made, longfg_attempted, longfg_made, xp_attempted,
                 xp_made, punt_attempts, punt_yards, punt_returns, punt_return_yards,
                 punt_return_touchdowns, kick_returns, kick_return_yards, kick_return_touchdowns,
                 team):
        if team is None:
            raise ValueError('\'team\' field cannot be left as None.')
        self.position = position
        self.first_name = first_name
        self.last_name = last_name
        self.games_played = games_played
        self.games_started = games_started
        self.passing_completions = passing_completions
        self.pass_attempts = pass_attempts
        self.passing_yards = passing_yards
        self.passing_touchdowns = passing_touchdowns
        self.interceptions_against = interceptions_against
        self.sacks_against = sacks_against
        self.fumbles_against = fumbles_against
        self.qbr = qbr
        self.rushing_attempts = rushing_attempts
        self.rushing_yards = rushing_yards
        self.rushing_touchdowns = rushing_touchdowns
        self.interceptions_for = interceptions_for
        self.pick_sixes = pick_sixes
        self.forced_fumbles_for = forced_fumbles_for
        self.fumble_recovery_for = fumble_recovery_for
        self.fumble_sixes = fumble_sixes
        self.passes_defended = passes_defended
        self.sacks_for = sacks_for
        self.total_tackles = total_tackles
        self.solo_tackles = solo_tackles
        self.tackles_for_loss = tackles_for_loss
        self.qb_hits = qb_hits
        self.fg_attempted = fg_attempted
        self.fg_made = fg_made
        self.longfg_attempted = longfg_attempted
        self.longfg_made = longfg_made
        self.xp_attempted = xp_attempted
        self.xp_made = xp_made
        self.punt_attempts = punt_attempts
        self.punt_yards = punt_yards
        self.punt_returns = punt_returns
        self.punt_return_yards = punt_return_yards
        self.punt_return_touchdowns = punt_return_touchdowns
        self.kick_returns = kick_returns
        self.kick_return_yards = kick_return_yards
        self.kick_return_touchdowns = kick_return_touchdowns
        self.team = team
