import sys
sys.path.append('..') 

import csv
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
myMongoClient = pymongo.MongoClient(MONGODB_URL)
db = myMongoClient["projetoimdb"]
yearCollection = db["yearCollection"]


def groupByYear():
    print("Realizando agrupamento...")
    with open("../ImdbTitleBasics.csv", "r", encoding="utf-8") as myFile:
        # Cada linha fica no formato coluna/valor
        read_csv = csv.DictReader(myFile)

        allYears = {}

        for line in read_csv:
            startYear = line["startYear"]
            if startYear not in allYears:
                allYears[startYear] = [line["tconst"]]
            else:
                allYears[startYear].append(line["tconst"])

        # for key in allYears:
        #    print("key: " + key + ", valueCounts: " + str(len(allYears[key])))

        print("Agrupamento finalizado.")
        return allYears


def insertAllYears(allYears):
    print("Gravando no MongoDB...")
    for key in allYears:
        yearCollection.insert_one({"year": key, "titles": allYears[key]})
    print("Finalizada escrita no MongoDB.")

insertAllYears(groupByYear())