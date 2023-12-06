import sys
sys.path.append("..")

from mongoConnection import getDBConnection

db = getDBConnection()
akasCollection = db["akasCollection"]
allTitlesCollection = db["allTitlesCollection"]


def getAkasByTitle(title):
    title = allTitlesCollection.find_one({'originalTitle':titleName})
    titleId = title['tconst']
    result = akasCollection.find_one({'titleId':titleId})
    print(f"Akas do título {titleId}")
    for aka in result['titles']:
        print(aka)

titleName = "Blacksmith Scene"

getAkasByTitle(titleName)