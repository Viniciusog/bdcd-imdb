LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleBasics.csv' AS row
WITH row 
SKIP 0 LIMIT 1000000
CREATE (:TitlePrincipal {
    tconst: row.tconst,
    titleType: toInteger(row.titleType),
    primaryTitle: row.primaryTitle,
    originalTitle: row.originalTitle,
    isAdult: toInteger(row.isAdult),
    startYear: toInteger(row.startYear),
    runtimeMinutes: toInteger(row.runtimeMinutes),
    genres: row.genres
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleBasics.csv' AS row
WITH row 
SKIP 1000000
CREATE (:TitlePrincipal {
    tconst: row.tconst,
    titleType: toInteger(row.titleType),
    primaryTitle: row.primaryTitle,
    originalTitle: row.originalTitle,
    isAdult: toInteger(row.isAdult),
    startYear: toInteger(row.startYear),
    runtimeMinutes: toInteger(row.runtimeMinutes),
    genres: row.genres
});