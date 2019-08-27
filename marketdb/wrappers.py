from marketdb.session import Base
from marketdb.models.nba import NBATeam, NBAPlayer

def initdb(engine):
    Base.metadata.create_all(engine)

def dropdb(engine):
    Base.metadata.drop_all(engine)

def new_nbaTeam(session, city='', team_name='', wins=0, losses=0,
                wins_lastYear=0, losses_lastYear=0, conference_standings=0,
                playoff_odds=0.0, starters_rating=0.0, bench_rating=0.0,
                points_for=0, field_goal=0.0, threePt_made=0, free_throw=0.0,
                offensive_rebounds=0, defensive_rebounds=0, assists=0, turnovers=0,
                plus_minus=0.0, points_against=0, steals=0, blocks=0):
    newteam = NBATeam(city, team_name, wins, losses, wins_lastYear,
                      losses_lastYear, conference_standings, playoff_odds,
                      starters_rating, bench_rating, points_for, field_goal,
                      threePt_made, free_throw, offensive_rebounds,
                      defensive_rebounds, assists, turnovers, plus_minus,
                      points_against, steals, blocks)
    session.add(newteam)
    session.commit()
    return newteam

def new_nbaPlayer(session, first_name='', last_name='', games_played=0,
                  games_started=0, points=0, field_goals_attemped=0,
                  field_goals_made=0, threePt_attempted=0, threePt_made=0,
                  freeThrows_attempted=0, freeThrows_made=0, assists=0,
                  turnovers=0, defensive_rebounds=0, offensive_rebounds=0,
                  plus_minus=0, min_per_game=0.0, win_share=0,
                  true_shooting_pct=0.0, fouls=0, blocks=0, team=None):
    newplayer = NBAPlayer(first_name, last_name, games_played, games_started,
                          points, field_goals_attemped, field_goals_made,
                          threePt_attempted, threePt_made, freeThrows_attempted,
                          freeThrows_made, assists, turnovers, defensive_rebounds,
                          offensive_rebounds, plus_minus, min_per_game, win_share,
                          true_shooting_pct, fouls, blocks, team)
    session.add(newplayer)
    session.commit()
    return newplayer

def new_nflTeam(session, city='', name='', wins=0, losses=0, ties=0, wins_lastYear=0,
                losses_lastYear=0, ties_lastYear=0, playoff_odds=0.0, team_rating=0.0,
                offense_rating=0.0, qb_rating=0.0, offensive_pointsFor=0, yards_for=0,
                touchdowns_for=0, offensive_redzone_eff=0.0, defense_rating=0.0,
                yards_against=0, points_against=0, touchdowns_against=0, sacks=0,
                interceptions=0, defensive_redzone_eff=0.0, defensive_pointsFor=0,
                defensive_eff=0):
    newteam = NFLTeam(city, name, wins, losses, ties, wins_lastYear, losses_lastYear,
                      ties_lastYear, playoff_odds, team_rating, offense_rating,
                      qb_rating, offensive_pointsFor, yards_for, touchdowns_for,
                      offensive_redzone_eff, defense_rating, yards_against, points_against,
                      touchdowns_against, sacks, interceptions, defensive_redzone_eff,
                      defensive_pointsFor, defensive_eff)
    session.add(newteam)
    session.commit()
    return newteam

def get_nbaTeam(session, team_name, city_name):
    return session.query(NBATeam) \
                  .filter(NBATeam.team_name == tname and \
                          NBATeam.city_name == cname) \
                  .first()

def get_players_on_nbaTeam(session, team_name, city_name):
    return get_nbaTeam(session, team_name, city_name).players

def get_nbaPlayer(session, first_name, last_name):
    return session.query(NBAPlayer) \
                  .filter(NBAPlayer.first_name == first_name and \
                          NBAPlayer.last_name == last_name) \
                  .first()
