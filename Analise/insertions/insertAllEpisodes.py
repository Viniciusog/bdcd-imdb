import sys
sys.path.append('..') 

from mongoConnection import getDBConnection
import csv

db = getDBConnection()
allEpisodesCollection = db["allEpisodesCollection"]

def insertAllEpisodes():
    print("Inicializando inserção - allEpisodesCollection")
    with open("../ImdbTitleEpisode.csv", "r", encoding="utf-8") as file:
        file_reader = csv.DictReader(file)
        # tconst,titleType,primaryTitle,originalTitle,isAdult,startYear,endYear,runtimeMinutes,genres
        for line in file_reader:
            #tconst,parentTconst,seasonNumber,episodeNumber
            currentEpisode = {
                'tconst':line['tconst'],
                'parentTconst':line['parentTconst'],
                'seasonNumber':line['seasonNumber'],
                'episodeNumber':line['episodeNumber']
            }
            allEpisodesCollection.insert_one(currentEpisode)
        print("Finalizando inserção - allEpisodesCollection")

insertAllEpisodes()
            
            