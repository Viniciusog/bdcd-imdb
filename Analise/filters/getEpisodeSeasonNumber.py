import sys
sys.path.append('..') 

from mongoConnection import getDBConnection
db = getDBConnection()
allEpisodesCollection = db["allEpisodesCollection"]

def getEpisodeSeasonNumber(episodeTconst):
    result = allEpisodesCollection.find_one({'tconst':episodeTconst})
    return result['seasonNumber']
    
seasonNumber = getEpisodeSeasonNumber("tt0043693")
print(seasonNumber)