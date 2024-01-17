import sys
sys.path.append('..') 

from mongoConnection import getDBConnection

db = getDBConnection()
allNamesCollection = db['allNamesCollection']

def getPersonByName(primaryName):
    myPerson = allNamesCollection.find({"primaryName":primaryName})
    return myPerson

person = getPersonByName("John Belushi")
for p in person:
    print(p)