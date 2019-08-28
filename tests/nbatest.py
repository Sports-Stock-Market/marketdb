from marketdb.session import engine, session
from marketdb.models.nba import NBATeam, NBAPlayer
from marketdb.wrappers import initdb, dropdb, \
                              new_nbaTeam, new_nbaPlayer, \
                              get_nbaTeam, get_nbaPlayer

Engine = engine()
Session = session(Engine)

initdb(Engine)

lakers = new_nbaTeam(Session, city='Los Angeles', team_name='Lakers')
clippers = new_nbaTeam(Session, city='Los Angeles', team_name='Clippers')
raptors = new_nbaTeam(Session, city='Toronto', team_name='Raptors')

kawhi = new_nbaPlayer(Session, first_name='Kawhi', last_name='Leonard', team=raptors)

assert kawhi in raptors.players

kawhi.team = clippers
Session.commit()

assert kawhi in clippers.players
assert kawhi not in raptors.players

Session.delete(kawhi)
Session.delete(lakers)
Session.delete(clippers)
Session.delete(raptors)
Session.commit()

assert len(Session.query(NBATeam).all()) == 0
assert len(Session.query(NBAPlayer).all()) == 0
