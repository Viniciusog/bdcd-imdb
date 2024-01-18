LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleCrew.csv' AS row 
WITH row
SKIP 0 LIMIT 1000000
CREATE (:TitleCrew {
  tconst: row.tconst,
  directors: row.directors,
  writers: row.writers,
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleCrew.csv' AS row 
WITH row
SKIP 1000000
CREATE (:TitleCrew {
  tconst: row.tconst,
  directors: row.directors,
  writers: row.writers,
});