import sys
sys.path.append("..")
import csv
from mongoConnection import getDBConnection

db = getDBConnection()
akasCollection = db['akasCollection']

def insertAllAkas():
    with open("../ImdbTitleAkas.csv", "r", encoding="utf-8") as file:
        file_reader = csv.DictReader(file)
        
        myDict = {}
        
        for line in file_reader:
            #titleId,ordering,title,region,language,types,attributes,isOriginalTitle
                
            currentAka = {
                'titleId': line['titleId'],
                'ordering': line['ordering'],
                'title': line['title'],
                'region': line['region'],
                'language': line['language'],
                'types': line['types'],
                'attributes': line['attributes'],
                'isOriginalTitle': line['isOriginalTitle']
            }
            
            if line['titleId'] not in myDict:
                myDict[line['titleId']] = [currentAka]
            else:
                myDict[line['titleId']].append(currentAka)
    
        for key in myDict:
            akasCollection.insert_one({'titleId':key, "titles":myDict[key]})

insertAllAkas()