import sys
sys.path.append('..')

from mongoConnection import getDBConnection

db = getDBConnection()
titleCrewCollection = db["titleCrewCollection"]

def getWritersByFilm(filmTconst):
    filmCrew = titleCrewCollection.find_one({'tconst':filmTconst})
    return filmCrew['writers']

print(getWritersByFilm('tt0000709'))