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
            currentPerson = PersonBasic('','','','','','')
            currentPerson.nconst = line['nconst']
            currentPerson.primaryName = line["primaryName"]
            currentPerson.birthYear = line["birthYear"]
            currentPerson.deathYear = line['deathYear']
            currentTitle.primaryProfession = line['primaryProfession']
            currentTitle.knownForTitles = line['knownForTitles'].split(',')

            allTitlesCollection.insert_one(currentPerson.__dict__)
        print("Finalizando inserção - allTitlesCollection")