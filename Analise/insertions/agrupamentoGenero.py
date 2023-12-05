from util import get_all_genres
import csv
from mongoConnection import getDBConnection

db = getDBConnection()
genresCollection = db["genresCollection"]


def groupByGenre():
    myGenres = get_all_genres()

    myDict = {}

    for genre in myGenres:
        myDict[genre] = []

    with open("./ImdbTitleBasics.csv",'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        for linha in leitor_csv:
            for currentGenre in linha['genres'].split(','):
                if currentGenre != "\\N":
                    myDict[currentGenre].append(linha['tconst'])
        

    for key in myDict.keys():
        print(f'{key}: {len(myDict[key])}')
    
    for key in myDict.keys():
        genresCollection.insert_one({'genre': key, 'titles': myDict[key]})
        
groupByGenre()