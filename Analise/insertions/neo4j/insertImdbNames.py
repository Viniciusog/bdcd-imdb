""" from neo4j import GraphDatabase

class MyNeo4jConnection():
    def __init__(self, uri, user, pwd):
        self.uri = uri
        self.user = user
        self.pwd = pwd
        
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.pwd))
        except Exception as e:
            print("Falha ao criar o drive: ", e)

    
    def close(self):
        if self.driver is not None:
            self.driver.close()
    
    def query(self, pQuery, parameters=None, db=None):
        assert self.driver is not None, "Driver não inicializado!"
        session = None
        response = None
        
        try:
            session = self.driver.session(database=db) if db is not None else self.drive.session()
            response = list(session.run(pQuery, parameters))
        except Exception as e:
            print("Query failed: ", e)
        finally:
            if session is not None:
                session.close()
        return response


conn = MyNeo4jConnection("bolt://localhost:7687", "neo4j","12345678")
response = conn.query("MATCH (n) RETURN n",None, "neo4j")
print(response)
 """
 
import pandas as pd
from py2neo import Graph

# Configuração do Neo4j
url = "bolt://localhost:7687"  # URL do Neo4j
username = "neo4j"       # Usuário do Neo4j
password = "12345678"         # Senha do Neo4j
graph = Graph(url, auth=(username, password))

# Lendo o arquivo CSV
csv_file = "./ImdbName.csv"
df = pd.read_csv(csv_file)

# Definindo o tamanho do lote
batch_size = 10000  # Ajuste conforme necessário

# Inserindo dados em lotes
for start in range(0, len(df), batch_size):
    end = start + batch_size
    batch = df.iloc[start:end]
    query = """
    UNWIND $rows AS row
    CREAsTE (n:ImdbName)
    SET n = row
    """
    graph.run(query, rows=batch.to_dict('records'))

print("Importação concluída.")        