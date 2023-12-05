import sys
sys.path.append("..")

from mongoConnection import getDBConnection

db = getDBConnection()
allEpisodesCollection = db["allEpisodesCollection"]

def getEpisodesByTitle(titleId):
    titleEpisodes = allEpisodesCollection.find({'parentTconst':titleId})
    print(f"Episódios do título {titleId}")
    for episode in titleEpisodes:
        print(f"Episode tconst: {episode['tconst']} - ParentTconst: {episode['parentTconst']}"+
              f" | seasonNumber: {episode['seasonNumber']} | episodeNumber: {episode['episodeNumber']}\n")

getEpisodesByTitle('tt0040051')