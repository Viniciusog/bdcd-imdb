import csv
import sys
sys.path.append("..")
from mongoConnection import getDBConnection

db = getDBConnection()
ratingsCollection = db["ratingsCollection"]

def insertAllRatings():
    print("Realizando inserções de avaliações...")
    with open("../ImdbTitleRatings.csv", "r", encoding="utf-8") as csv_file:
        read_csv = csv.DictReader(csv_file)

        for line in read_csv:
            ratingsCollection.insert_one({"tconst": line['tconst'], "averageRating": line['averageRating'], "numVotes": line['numVotes']})
            
        #print(ratings[5])
        print("Inserções finalizadas.")

insertAllRatings()