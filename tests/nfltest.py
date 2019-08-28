from marketdb.session import engine, session
from marketdb.models.nfl import NFLTeam, NFLPlayer
from marketdb.wrappers import initdb, dropdb, \
                              new_nflTeam, new_nflPlayer, \
                              get_nflTeam, get_nflPlayer

Engine = engine()
Session = session(Engine)

initdb(Engine)

giants = new_nflTeam(Session, city='New York', team_name='Giants')
browns = new_nflTeam(Session, city='Cleveland', team_name='Browns')

odell = new_nflPlayer(Session, first_name='Odell', last_name='Beckham Jr.', team=giants)

assert odell in giants.players

odell.team = browns
Session.commit()

assert odell in browns.players
assert odell not in giants.players

Session.delete(odell)
Session.delete(giants)
Session.delete(browns)
Session.commit()

assert len(Session.query(NFLTeam).all()) == 0
assert len(Session.query(NFLPlayer).all()) == 0
