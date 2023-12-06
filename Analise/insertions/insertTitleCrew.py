import sys
sys.path.append('..')

from mongoConnection import getDBConnection
import csv

db = getDBConnection()
titleCrewCollection = db["titleCrewCollection"]

def insertTitleCrew():
    print("Inicializando inserção - titleCrewCollection")
    with open("../ImdbTitleCrew.csv", "r", encoding="utf-8") as file:
        file_reader = csv.DictReader(file)
        # tconst,directors,writers
        for line in file_reader:
            currentTitleCrew = {
                'tconst':line['tconst'],
                'directors':line['directors'],
                'writers':line['writers']
            }
            titleCrewCollection.insert_one(currentTitleCrew)
        print("Finalizando inserção - titleCrewCollection")

insertTitleCrew()