import sys
sys.path.append("..")

from mongoConnection import getDBConnection

db = getDBConnection()
genresCollection = db["genresCollection"]

def filterByGenre(genre):
    titles = genresCollection.find(genre)
    
    print(f"{genre} titles: ")
    for title in titles:
        print(f"{title}\n")

genre = "Short"
title = filterByGenre(genre)
