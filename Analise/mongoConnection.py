import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
myMongoClient = pymongo.MongoClient(MONGODB_URL)
db = myMongoClient["projetoimdb"]
mainCollection = db["main"]
testCollection = db["testCollection"]
testYearCollection = db["testYearCollection"]

def getMongoConnection():
    return myMongoClient

def getDBConnection():
    return db