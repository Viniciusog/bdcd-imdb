from util import get_all_genres
import csv
import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
myMongoClient = pymongo.MongoClient(MONGODB_URL)
db = myMongoClient['projetoimdb']
mainCollection = db['main']
testCollection = db['testCollection']
testYearCollection = db['testYearCollection']

def agruparAno():
    print("Realizando agrupamento...")
    with open("./ImdbTitleBasics.csv", "r", encoding="utf-8") as arquivo:
        # Cada linha fica no formato coluna/valor
        leitor_csv = csv.DictReader(arquivo)

        allYears = {}

        for linha in leitor_csv:
            startYear = linha['startYear']
            if startYear not in allYears:
                allYears[startYear] = [linha['tconst']]
            else:
                allYears[startYear].append(linha['tconst'])

        #for key in allYears:
        #    print("key: " + key + ", valueCounts: " + str(len(allYears[key])))
        
        print("Agrupamento finalizado.")
        return allYears
    
def inserirAllYears(allYears):
    print("Gravando no MongoDB...")
    for key in allYears:
        testYearCollection.insert_one({'year':key, 'titles':allYears[key]})
    print("Finalizada escrita no MongoDB.")

inserirAllYears(agruparAno())