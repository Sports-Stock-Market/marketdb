from marketdb.session import Base
from marketdb.models.nba import NBATeam, NBAPlayer, NFLTeam, NFLPlayer

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

def new_nflPlayer(session, position=0, first_name='', last_name='', games_played=0,
                  games_started=0, passing_completions=0, pass_attempts=0, passing_yards=0,
                  passing_touchdowns=0, interceptions_against=0, sacks_against=0,
                  fumbles_against=0, qbr=0.0, rushing_attempts=0, rushing_yards=0, rushing_touchdowns=0,
                  receiving_targets=0, receptions=0, receiving_yards=0, receiving_touchdowns=0,
                  interceptions_for=0, pick_sixes=0, forced_fumbles_for=0, fumble_recovery_for=0,
                  fumble_sixes=0, passes_defended=0, sacks_for=0, total_tackles=0, solo_tackles=0,
                  tackles_for_loss=0, qb_hits=0, fg_attempted=0, fg_made=0, longfg_attempted=0,
                  longfg_made=0, xp_attempted=0, xp_made=0, punt_attempts=0, punt_yards=0,
                  punt_returns=0, punt_return_yards=0, punt_return_touchdowns=0, kick_returns=0,
                  kick_return_yards=0, kick_return_touchdowns=0, team=None):
    newplayer = NFLPlayer(position, first_name, last_name, games_played, games_started,
                          passing_completions, pass_attempts, passing_yards, passing_touchdowns,
                          interceptions_against, sacks_against, fumbles_against, qbr,
                          rushing_attempts, rushing_yards, rushing_touchdowns, receiving_targets,
                          receptions, receiving_yards, receiving_touchdowns, interceptions_for,
                          pick_sixes, forced_fumbles_for, fumble_recovery_for, fumble_sixes,
                          passes_defended, sacks_for, total_tackles, solo_tackles, tackles_for_loss,
                          qb_hits, fg_attempted, fg_made, longfg_attempted, longfg_made, xp_attempted,
                          xp_made, punt_attempts, punt_yards, punt_returns, punt_return_yards,
                          punt_return_touchdowns, kick_returns, kick_return_yards, kick_return_touchdowns,
                          team)
    session.add(newplayer)
    session.commit()
    return newplayer

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

def get_nflTeam(session, team_name, city_name):
    return session.query(NFLTeam) \
                  .filter(NFLTeam.team_name == tname and \
                          NFLTeam.city_name == cname) \
                  .first()

def get_players_on_nflTeam(session, team_name, city_name):
    return get_nflTeam(session, team_name, city_name).players

def get_nflPlayer(session, first_name, last_name):
    return session.query(NFLPlayer) \
                  .filter(NFLPlayer.first_name == first_name and \
                          NFLPlayer.last_name == last_name) \
                  .first()
