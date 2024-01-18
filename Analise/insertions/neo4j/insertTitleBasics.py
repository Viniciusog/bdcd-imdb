import pandas as pd
from py2neo import Graph

# Configuração do Neo4j
url = "bolt://localhost:7687"  # URL do Neo4j
username = "neo4j"       # Usuário do Neo4j
password = "12345678"         # Senha do Neo4j
graph = Graph(url, auth=(username, password))

# Lendo o arquivo CSV
csv_file = "../../ImdbTitleBasics.csv"
df = pd.read_csv(csv_file)

# Definindo o tamanho do lote
batch_size = 10000  # Ajuste conforme necessário

# Inserindo dados em lotes
for start in range(0, len(df), batch_size):
    end = start + batch_size
    batch = df.iloc[start:end]
    query = """
    UNWIND $rows AS row
    CREATE (n:ImdbTitleBasics)
    SET n = row
    """
    graph.run(query, rows=batch.to_dict('records'))

print("Importação concluída.")        