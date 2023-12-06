import sys
sys.path.append('..') 

from mongoConnection import getDBConnection
from main import TitleBasic
import csv

db = getDBConnection()
allTitlesCollection = db["allTitlesCollection"]

def insertAllTitles():
    print("Inicializando inserção - allTitlesCollection")
    with open("../ImdbTitleBasics.csv", "r", encoding="utf-8") as file:
        file_reader = csv.DictReader(file)
        # tconst,titleType,primaryTitle,originalTitle,isAdult,startYear,endYear,runtimeMinutes,genres
        for line in file_reader:
            currentTitle = TitleBasic('','','','',False,'','','',[])
            currentTitle.tconst = line['tconst']
            currentTitle.titleType = line["titleType"]
            currentTitle.primaryTitle = line["primaryTitle"]
            currentTitle.originalTitle = line['originalTitle']
            if line["isAdult"] == 0:
                currentTitle.isAdult = False
            else:
                currentTitle.isAdult = True
            currentTitle.startYear = line['startYear']
            currentTitle.endYear = line['endYear']
            currentTitle.runtimeMinutes = line['runtimeMinutes']
            currentTitle.genres = line['genres'].split(',')
            allTitlesCollection.insert_one(currentTitle.__dict__)
        print("Finalizando inserção - allTitlesCollection")

insertAllTitles()
            
            