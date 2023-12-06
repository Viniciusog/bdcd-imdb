import csv
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
myMongoClient = pymongo.MongoClient(MONGODB_URL)
db = myMongoClient["projetoimdb"]
ratingsCollection = db["ratingsCollection"]


def groupByRating():
    print("Realizando agrupamento...")
    with open("./ImdbTitleRatings.csv", "r", encoding="utf-8") as csv_file:
        read_csv = csv.DictReader(csv_file)

        ratings = {}

        for line in read_csv:
            title_rating = int(float(line["averageRating"]))

            #tconst,averageRating,numVotes
            if title_rating not in ratings:
                ratings[title_rating] = []

            ratings[title_rating].append((line['tconst'], line['averageRating'], line['numVotes']))
            
        #print(ratings[5])
        print("Agrupamento finalizado.")
        return ratings


def insertRatings(ratings):
    print("Gravando no MongoDB...")
    for rating in ratings: #percorre a avaliação
        for title in rating: #percorre os títulos da avaliação
            tconst, avgRating, numVotes = title
            ratingsCollection.insert_one({"tconst": tconst, "avgRating": avgRating, "numVotes": numVotes})
    
    print("Finalizada escrita no MongoDB.")

#insertRatings()
groupByRating()
