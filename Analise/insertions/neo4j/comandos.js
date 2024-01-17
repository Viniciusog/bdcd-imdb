// * INSERIR OS DADOS
LOAD CSV WITH HEADERS FROM 'file:///ImdbName.csv' AS row
WITH row LIMIT 100
CREATE (n:ImdbName)
SET n.nconst = row.nconst,
    n.primaryName = row.primaryName,
    n.birthYear = row.birthYear,
    n.deathYear = row.deathYear,
    n.primaryProfession = row.primaryProfession,
    n.knownForTitles = row.knownForTitles

    
// * Retornar a quantidade de nós
MATCH (n:ImdbName)
RETURN count(n) AS TotalNodes


// * Retornar todos os nós
MATCH (n:ImdbName)
RETURN n


// * Esse comando faz: Para cada linha, vai na coluna knownForTitles, e retorna o id da pessoa junto com o id do filme que estava separado por vírgula (É importante para depois conseguir realizar as relações)
MATCH (n:ImdbName)
UNWIND split(n.knownForTitles, ',') AS titleId
RETURN n.nconst, titleId


// * Deletar todos os nós do tipo ImdbName
MATCH (n:ImdbName)
DELETE n




