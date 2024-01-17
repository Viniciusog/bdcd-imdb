LOAD CSV WITH HEADERS FROM 'file:///ImdbName.csv' AS row
WITH row 
SKIP 0 LIMIT 1000000
CREATE (:ImdbName {
    nconst: row.nconst,
    primaryName: row.primaryName,
    birthYear: toInteger(row.birthYear),
    deathYear: toInteger(row.deathYear),
    primaryProfession: row.primaryProfession,
    knownForTitles: row.knownForTitles
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbName.csv' AS row
WITH row 
SKIP 1000000 
CREATE (:ImdbName {
    nconst: row.nconst,
    primaryName: row.primaryName,
    birthYear: toInteger(row.birthYear),
    deathYear: toInteger(row.deathYear),
    primaryProfession: row.primaryProfession,
    knownForTitles: row.knownForTitles
});
