from marketdb.session import engine, session
from marketdb.wrappers import initdb, new_nbaTeam

'''
    Create an engine to initialize the mySQL database. This
    function assumes that your .env file is located in the same
    directory as the active program, and that it is actually named
    '.env'. If this is not the case, specify otherwise.
'''
Engine = engine(env_path='.env')

'''
    IMPORTANT: Any code you have making DB queries must have a
               session defined. Although you can make a new session
               everytime you query the DB, it is good practice to keep
               the same session active throughout the runtime of your
               program.
'''
Session = session(Engine)

'''
    Initialize mySQL database. This only needs to be done
    once if the DB hasn't been set up, and doesn't need to be
    done at all if the DB has been set up.
'''
initdb(Engine)

'''
    Create a NBA team and keep a hold of its 'NBATeam' instance.
    REMEMBER: the first argument of any query must be the active
              session!
'''
bucks = new_nbaTeam(Session, team_name='Bucks', city='Milwaukee', wins=5, losses=5,
                    wins_lastYear=5, losses_lastYear=5, conference_standings=1,
                    playoff_odds=.5, starters_rating=2, bench_rating=4, points_for=20,
                    field_goal=4, threePt_made=3, free_throw=1, offensive_rebounds=1,
                    defensive_rebounds=1, assists=1, turnovers=1, plus_minus=1,
                    points_against=1, steals=1, blocks=1)

'''
    Print its ID within the database just to make sure it's there.
'''
print(bucks.id)
