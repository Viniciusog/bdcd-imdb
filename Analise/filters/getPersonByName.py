import sys
sys.path.append('..') 

from mongoConnection import getDBConnection

db = getDBConnection()
allNamesCollection = db['allNamesCollection']

def getPersonByName(primaryName):
    myPerson = allNamesCollection.find_one({"primaryName":primaryName})
    return myPerson