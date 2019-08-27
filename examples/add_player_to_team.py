from marketdb.session import engine, session
from marketdb.wrappers import get_nbaTeam, new_nbaPlayer, \
                              get_players_on_nbaTeam

'''
    As always, we create our engine and session.
'''
Engine = engine()
Session = session(Engine)

'''
    We added the Bucks to the DB in 'create_team.py',
    so let's see if it's still in the DB.
'''
bucks = get_nbaTeam(Session, 'Bucks', 'Milwaukee')
print(bucks)

'''
    We can't just have a team without players, of course. Let's
    add everyone's favorite Greek to the team.
'''
giannis = new_nbaPlayer(Session, first_name='Giannis', last_name='Antetokounmpo',
                        games_started=1, points=1000000, field_goals_attemped=20,
                        field_goals_made=21, threePt_attempted=1, threePt_made=2,
                        freeThrows_attempted=0, freeThrows_made=1, assists=10,
                        turnovers=0, defensive_rebounds=1000, offensive_rebounds=1001,
                        plus_minus=0, min_per_game=60, win_share=0, true_shooting_pct=1.0,
                        fouls=0, blocks=100, team=bucks)

'''
    Now, let's make sure the DB knows Giannis belongs to the Bucks.
'''
assert giannis in bucks.players
