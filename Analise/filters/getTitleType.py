import sys
sys.path.append('..') 

from mongoConnection import getDBConnection

db = getDBConnection()
allTitlesCollection  = db['allTitlesCollection']

def getTitleType(titleId):
    myTitle = allTitlesCollection.find_one({'tconst':titleId})
    return myTitle['titleType']

titleId = "tt0239639"
titleType = getTitleType(titleId)
print(f"Title type for {titleId}: {titleType}")