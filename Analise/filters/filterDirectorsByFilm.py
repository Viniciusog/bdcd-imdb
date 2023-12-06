import sys
sys.path.append("..")

from mongoConnection import getDBConnection

db = getDBConnection()
titleCrewCollection = db["titleCrewCollection"]

def getDirectorsByFilm(filmTconst):
    filmCrew = titleCrewCollection.find_one({'tconst':filmTconst})
    return filmCrew['directors']

print(getDirectorsByFilm('tt0000001'))