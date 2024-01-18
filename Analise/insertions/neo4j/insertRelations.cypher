//TitleBasics -> TitleRatings

MATCH (n:TitleBasics), (m:TitleRatings)
WHERE n.tconst = m.tconst
MERGE (n)-[:AVALIADO_EM]->(m)
MERGE (m)-[:AVALIA]->(n);


//TitleBasics -> TitlePrincipals

MATCH (n:TitleBasics), (m:TitlePrincipals)
WHERE n.tconst = m.tconst
MERGE (n)-[:CONTOU_COM]->(m)
MERGE (m)-[:TRABALHOU_EM]->(n);


//TitleBasics -> TitleEpisodes

MATCH (n:TitleBasics), (m:TitleEpisodes)
WHERE n.tconst = m.tconst
MERGE (n)-[:APRESENTA]->(m)
MERGE (m)-[:FAZ_PARTE_DE]->(n);

//TitleAka -> TitleBasics

MATCH (aka:ImdbTitleAka), (basic:ImdbTitleBasic)
WHERE aka.titleId = basic.tconst
MERGE (aka)-[:ALSO_KNOWN_AS]->(basic);
