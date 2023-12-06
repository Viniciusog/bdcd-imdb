import sys

sys.path.append("..")

from mongoConnection import getDBConnection

db = getDBConnection()
allTitlesCollection = db["allTitlesCollection"]


def getFilmByTitle(title_string):
    myTitle = allTitlesCollection.find_one({"originalTitle": title_string})
    return myTitle


title_string = "The Matrix"
film = getFilmByTitle(title_string)
print(
    "Film: %s | id: %s | type: %s | genres: %s | startYear: %s | endYear: %s | runtimeMinutes: %s"
    % (
        film["originalTitle"],
        film["tconst"],
        film["titleType"],
        film["genres"],
        film["startYear"],
        film["endYear"],
        film["runtimeMinutes"],
    )
)
