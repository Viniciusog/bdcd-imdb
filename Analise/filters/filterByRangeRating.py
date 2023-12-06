import sys
sys.path.append('..') 

from mongoConnection import getDBConnection

db = getDBConnection()
ratingCollection = db['ratingCollection']

def filterByRatingRange():
    print("ok")
    first_rating = "5.2"
    last_rating = "5.5"
    
    filter = {'rating': {'$gte': first_rating, "$lte": last_rating}}
    
    results = ratingCollection.find(filter)
    for result in results:
        print("Rating: " + str(result['rating']) + "\nTitles: " + str(result['titles']) + "\n")    

filterByRatingRange()