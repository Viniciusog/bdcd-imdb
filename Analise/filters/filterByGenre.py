import sys
sys.path.append("..")

from mongoConnection import getDBConnection

db = getDBConnection()
genresCollection = db["genresCollection"]

def filterByGenre(genre):
    obj = genresCollection.find_one({'genre': genre})
    
    print(f"{genre} titles: ")
    for title in obj['titles']:
        print(f"{title['tconst']}")

genre = "Short"
title = filterByGenre(genre)
