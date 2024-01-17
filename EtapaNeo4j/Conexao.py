from neo4j import GraphDatabase

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

        