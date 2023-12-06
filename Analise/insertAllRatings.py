import sys
sys.path.append('..') 

from mongoConnection import getDBConnection
import csv

db = getDBConnection()
allRatingsCollection = db["allRatingsCollection"]

def insertAllRatings():
    print("Inicializando inserção - allRatingsCollection")
    with open("../ImdbTitleEpisode.csv", "r", encoding="utf-8") as file:
        file_reader = csv.DictReader(file)
        
        for line in file_reader: #tconst,averageRating,numVotes
            currentRating = {
                'tconst':line['tconst'],
                'averageRating':line['averageRating'],
                'numVotes':line['numVotes'],
            }
            allRatingsCollection.insert_one(currentRating)
        print("Finalizando inserção - allRatingsCollection")

insertAllRatings()
            
            