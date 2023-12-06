import sys
sys.path.append('..') 

from mongoConnection import getDBConnection
import csv

db = getDBConnection()
allNamesCollection = db["allNamesCollection"]

def insertAllNames():
    print("Inicializando inserção - allNamesCollection")
    with open("../ImdbName.csv", "r", encoding="utf-8") as file:
        file_reader = csv.DictReader(file)
        # nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles
        
        for line in file_reader:
            
            currentEpisode = {
                'nconst':line['nconst'],
                'primaryName':line['primaryName'],
                'birthYear':line['birthYear'],
                'deathYear':line['deathYear'],
                'primaryProfession':line['primaryProfession'].split(','),
                'knownForTitles':line['knownForTitles'].split(',')
            }

            allNamesCollection.insert_one(currentEpisode)
        print("Finalizando inserção - allNamesCollection")


insertAllNames()