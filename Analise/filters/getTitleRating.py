import sys
sys.path.append("..")
from mongoConnection import getDBConnection

db = getDBConnection()


ratingCollection = db['ratingsCollection']
def getTitleRating(titleId):
    myTitle = ratingCollection.find_one({'tconst':titleId})
    return myTitle

titleId = "tt0239639"
titleRating = getTitleRating(titleId)
print(f"Title: {titleRating}")    