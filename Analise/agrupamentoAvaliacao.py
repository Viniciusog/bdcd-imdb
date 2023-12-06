import csv
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
myMongoClient = pymongo.MongoClient(MONGODB_URL)
db = myMongoClient["projetoimdb"]
ratingCollection = db["ratingCollection"]


def groupByRating():
    print("Realizando agrupamento...")
    with open("./ImdbTitleRatings.csv", "r", encoding="utf-8") as csv_file:
        read_csv = csv.DictReader(csv_file)

        ratings = {}

        for line in read_csv:
            movie_rating = int(float(line["averageRating"]))

            if movie_rating not in ratings:
                ratings[movie_rating] = [] 

            ratings[movie_rating].append(line['tconst'])
            
        print(ratings[1])

        print("Agrupamento finalizado.")
        return ratings


def insertRatings(ratings):
    print("Gravando no MongoDB...")
    for key in ratings:
        ratingCollection.insert_one({"rating": key, "titles": ratings[key]})
    print("Finalizada escrita no MongoDB.")

groupByRating()