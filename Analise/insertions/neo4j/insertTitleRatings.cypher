LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleRatings.csv' AS row
WITH row 
SKIP 0 LIMIT 1000000
CREATE (:TitlePrincipal {
    tconst: row.tconst,
    averageRating: toFloat(row.averageRating),
    numVotes: toInteger(row.numVotes)
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleRatings.csv' AS row
WITH row 
SKIP 1000000
CREATE (:TitlePrincipal {
    tconst: row.tconst,
    averageRating: toFloat(row.averageRating),
    numVotes: toInteger(row.numVotes)
});