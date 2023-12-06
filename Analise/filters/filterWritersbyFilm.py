import sys
sys.path.append('..')

from mongoConnection import MongoConnection

db = getDBConnection()
titleCrewCollection = db["titleCrewCollection"]

def getWritersByFilm(filmTconst):
    filmCrew = titleCrewCollection.find_one({'tconst':filmTconst})
    return filmCrew['writers']

print(getWriterssByFilm('tt0000001'))