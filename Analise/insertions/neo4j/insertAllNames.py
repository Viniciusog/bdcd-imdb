from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
username = "neo4j"
password = "neo4j"


csv_file_path = "../../ImdbName.csv"

with open(csv_file_path, "r") as file:
    # Skip the header row
    header = file.readline().strip().split(",")
    
    # Create a Cypher query template
    query_template = f"CREATE (:label {{ {', '.join([f'{property}: row.{property}' for property in header])} }});"

    with GraphDatabase.driver(uri, auth=(username, password)) as driver:
        with driver.session() as session:
            # Iterate through each line in the CSV file
            for line in file:
                # Create a dictionary with column names as keys and row values as values
                row_values = dict(zip(header, line.strip().split(",")))

                # Execute the Cypher query for each row
                session.run(query_template, row=row_values)