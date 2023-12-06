import sys
sys.path.append("..")
import csv
from mongoConnection import getDBConnection

db = getDBConnection()
allTitlesCollection = db["allTitlesCollection"]

def getTitleById(tconst):
    result = allTitlesCollection.find_one({'tconst':tconst})
    print(result)
    
getTitleById("tt0239639")
        
        