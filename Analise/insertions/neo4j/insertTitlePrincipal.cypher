LOAD CSV WITH HEADERS FROM 'file:///ImdbTitlePrincipal.csv' AS row
WITH row 
SKIP 0 LIMIT 1000000
CREATE (:TitlePrincipal {
    tconst: row.tconst,
    ordering: toInteger(row.ordering),
    nconst: row.nconst,
    category: row.category,
    job: row.job,
    characters: row.characters
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitlePrincipal.csv' AS row
WITH row 
SKIP 1000000
CREATE (:TitlePrincipal {
    tconst: row.tconst,
    ordering: toInteger(row.ordering),
    nconst: row.nconst,
    category: row.category,
    job: row.job,
    characters: row.characters
})