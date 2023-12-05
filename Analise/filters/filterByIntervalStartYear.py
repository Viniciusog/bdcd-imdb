import sys
sys.path.append('..') 

from mongoConnection import getDBConnection

db = getDBConnection()
yearCollection = db['yearCollection']

def filterByIntervalStartYear():
    print("ok")
    firstStartYear = "1896"
    secondStartYear = "1900"
    
    myFilter = {'year': {'$gte': firstStartYear, "$lte": secondStartYear}}
    
    results = yearCollection.find(myFilter)
    for result in results:
        print("Year: " + str(result['year']))    

filterByIntervalStartYear()