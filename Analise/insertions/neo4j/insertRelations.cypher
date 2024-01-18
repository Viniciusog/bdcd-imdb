//TitleBasics -> TitleRatings

MATCH (n:TitleBasics), (m:TitleRatings)
WHERE n.nconst = m.nconst
MERGE (n)-[:AVALIADO_EM]->(m)
MERGE (m)-[:AVALIA]->(n);


//TitleBasics -> TitlePrincipals

MATCH (n:TitleBasics), (m:TitlePrincipals)
WHERE n.nconst = m.nconst
MERGE (n)-[:CONTOU_COM]->(m)
MERGE (m)-[:TRABALHOU_EM]->(n);


//TitleBasics -> TitleEpisodes

MATCH (n:TitleBasics), (m:TitleEpisodes)
WHERE n.nconst = m.nconst
MERGE (n)-[:APRESENTA]->(m)
MERGE (m)-[:FAZ_PARTE_DE]->(n);
