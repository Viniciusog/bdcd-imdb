import csv
import pymongo
from dotenv import load_dotenv
import os
from util import get_all_genres

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
myMongoClient = pymongo.MongoClient(MONGODB_URL)
db = myMongoClient['projetoimdb']
mainCollection = db['main']
genresCollection = db['genresCollection']
testCollection = db['testCollection']

class TitleBasic:
    def __init__(self, tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres):
        self.tconst = tconst
        self.titleType = titleType
        self.primaryTitle = primaryTitle
        self.originalTitle = originalTitle
        self.isAdult = isAdult
        self.startYear = startYear
        self.endYear = endYear
        self.runtimeMinutes = runtimeMinutes
        self.genres = genres

    def __str__(self):
        return f'tconst: {self.tconst}, titleType: {self.titleType}, primaryTitle: {self.primaryTitle}, originalTitle: {self.originalTitle}, isAdult: {self.isAdult}, startYear: {self.startYear}, endYear: {self.endYear}, runtimeMinutes: {self.runtimeMinutes}, genres: {self.genres}'

    def get_tconst(self):
        return self.tconst

    def get_titleType(self):
        return self.titleType

    def get_primaryTitle(self):
        return self.primaryTitle

    def get_originalTitle(self):
        return self.originalTitle

    def get_isAdult(self):
        return self.isAdult

    def get_startYear(self):
        return self.startYear

    def get_endYear(self):
        return self.endYear

    def get_runtimeMinutes(self):
        return self.runtimeMinutes

    def get_genres(self):
        return self.genres

    def set_tconst(self, novo_tconst):
        self.tconst = novo_tconst

    def set_titleType(self, novo_titleType):
        self.titleType = novo_titleType

    def set_primaryTitle(self, novo_primaryTitle):
        self.primaryTitle = novo_primaryTitle

    def set_originalTitle(self, novo_originalTitle):
        self.originalTitle = novo_originalTitle

    def set_isAdult(self, novo_isAdult):
        self.isAdult = novo_isAdult

    def set_startYear(self, novo_startYear):
        self.startYear = novo_startYear

    def set_endYear(self, novo_endYear):
        self.endYear = novo_endYear

    def set_runtimeMinutes(self, novo_runtimeMinutes):
        self.runtimeMinutes = novo_runtimeMinutes

    def set_genres(self, novos_genres):
        self.genres = novos_genres

def inserir_mongodb():
    with open("./ImdbTitleBasics.csv", 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        colunas = leitor_csv.fieldnames

        cont = 0

        for coluna in colunas:
            print(coluna)

        allGenres = {}

        #while cont < 10:
        for linha in leitor_csv:
            # linha = next(leitor_csv)
            titleBasic = TitleBasic('', '', '', '', False, '', '', '', [])

            for key, value in linha.items():
                myValue = value

                if key == 'genres':            
                    myValue = value.split(',')

                    for myGenre in myValue:
                        if myGenre not in allGenres:
                            allGenres[myGenre] = 1
                        else:
                            allGenres[myGenre] = (allGenres[myGenre] + 1)
                

                setattr(titleBasic, key, myValue)

            # result = mainCollection.insert_one(titleBasic.__dict__)
            #print(f"Object inserted: {result}")
            # print(linha)
            #cont += 1
        
        print(allGenres)




class GenreDoc:
    def __init__(self, genre, titles):
        self.genre = genre
        self.titles = titles
        
def populateGenres():
    genresArray = get_all_genres() 

    for currentGenre in genresArray:
        myObjectGenre = GenreDoc(currentGenre, [])
        genresCollection.insert_one(myObjectGenre.__dict__)

# Extremamente demorado
def addTitlesToGenresCollection():
    with open("./ImdbTitleBasics.csv", 'r', encoding='utf-8') as arquivo_csv :
        leitor_csv = csv.DictReader(arquivo_csv)

        cont = 0
        contTitle = 0

        for linha in leitor_csv:
            for genre in linha['genres'].split(','):
                if genre != "\\N": 
                    result = genresCollection.update_one({'genre': genre}, 
                                                         {'$push': {'titles': {'tconst':linha['tconst']}}})
                    if result.modified_count > 0:                        
                        cont += 1
                    else:
                        print("Documento não foi atualizado")    
            contTitle += 1
        print(f"Alterados: {cont}")
        print(f'contTitle: {contTitle}')

# Muito rápido
def addTitlesToTestCollection():
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
        testCollection.insert_one({'genre': key, 'titles': myDict[key]})

    print("alguma coisa")
    
#get_all_genres()
#populateGenres()
#inserir_mongodb()
#addTitlesToGenresCollection()
#inserir_mongodb()
#populateGenres()
#addTitlesToGenresCollection()
#addTitlesToTestCollection()