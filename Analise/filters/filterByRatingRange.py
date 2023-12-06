import sys
sys.path.append('..') 

from mongoConnection import getDBConnection

db = getDBConnection()
ratingCollection = db['ratingsCollection']

def filterByRatingRange(first_rating, last_rating):

    filter = {'averageRating': {'$gte': first_rating, "$lte": last_rating}}

    results = ratingCollection.find(filter)
    for result in results:
        print(f"Title id: {str(result['tconst'])}, Title rating: {str(result['averageRating'])}, Total votes: {str(result['numVotes'])}\n")    

first_rating = "5.2"
last_rating = "5.5"
filterByRatingRange(first_rating, last_rating)