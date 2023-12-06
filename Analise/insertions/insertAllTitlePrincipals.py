import sys
sys.path.append('..')

from mongoConnection import getDBConnection
import csv

db = getDBConnection()
titlePrincipalsCollection = db["titlePrincipalsCollection"]

def insertAllTitlePrincipals():
    print("Inicializando inserção - titlePrincipalsCollection")
    with open("../ImdbTitlePrincipals.csv", "r", encoding="utf-8") as file:
        file_reader = csv.DictReader(file)
        # tconst,ordering,nconst,category,job,characters
        for line in file_reader:
            currentTitlePrincipals = {
                'tconst':line['tconst'],
                'ordering':line['ordering'],
                'nconst':line['nconst'],
                'category':line['category'],
                'job':line['job'],
                'characters':line['characters']
            }
            titlePrincipalsCollection.insert_one(currentTitlePrincipals)
        print("Finalizando inserção - titlePrincipalsCollection")

insertAllTitlePrincipals()