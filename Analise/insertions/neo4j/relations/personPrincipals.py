from py2neo import Graph
import csv

# Conexão com o banco de dados Neo4j
graph = Graph("neo4j://localhost:7687", auth=("neo4j", "12345678"))

# Função para criar relações a partir do arquivo ImdbPrincipals
def create_relationships_from_imdb_principals(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            query = """
            MATCH (p:ImdbName {nconst: $nconst})
            MERGE (principal:ImdbTitlePrincipals {nconst: $nconst})
            MERGE (p)-[:RE_PERSON_PRINCIPAL]->(principal)
            """
            graph.run(query, nconst=row['nconst'])
            

create_relationships_from_imdb_principals("../../../ImdbTitlePrincipals.csv")