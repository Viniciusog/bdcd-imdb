import sys
sys.path.append('..') 

from mongoConnection import getDBConnection

db = getDBConnection()
titlePrincipalsCollection = db['titlePrincipalsCollection']

def getPrincipalsByTitle(t_id):
    principalsArray = titlePrincipalsCollection.find({"tconst" = t_id})
    return principalsArray

#teste hardcoded
arrayPrincipals = getPrincipalsByTitle("tt0000009")

for pessoa in arrayPrincipals:
    print(f"ID da pessoa: {pessoa['nconst']}\n")
    print(f"Categoria: {pessoa['category']}\n")
    print(f"Profissao: {pessoa['job']}\n")
    print(f"Personagem: {pessoa['characters']}\n\n")