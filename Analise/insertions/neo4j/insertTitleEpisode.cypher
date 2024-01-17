LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleEpisode.csv' AS row 
WITH row
SKIP 0 LIMIT 1000000
CREATE (:TitleEpisode {
  tconst: row.tconst,
  parentTconst: row.parentTconst,
  seasonNumber: toInteger(row.seasonNumber),
  episodeNumber: toInteger(row.episodeNumber)
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleEpisode.csv' AS row 
WITH row
SKIP 1000000 LIMIT 1000000
CREATE (:TitleEpisode {
  tconst: row.tconst,
  parentTconst: row.parentTconst,
  seasonNumber: toInteger(row.seasonNumber),
  episodeNumber: toInteger(row.episodeNumber)
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleEpisode.csv' AS row 
WITH row
SKIP 2000000 LIMIT 1000000
CREATE (:TitleEpisode {
  tconst: row.tconst,
  parentTconst: row.parentTconst,
  seasonNumber: toInteger(row.seasonNumber),
  episodeNumber: toInteger(row.episodeNumber)
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleEpisode.csv' AS row 
WITH row
SKIP 3000000 LIMIT 1000000
CREATE (:TitleEpisode {
  tconst: row.tconst,
  parentTconst: row.parentTconst,
  seasonNumber: toInteger(row.seasonNumber),
  episodeNumber: toInteger(row.episodeNumber)
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleEpisode.csv' AS row 
WITH row
SKIP 4000000 LIMIT 1000000
CREATE (:TitleEpisode {
  tconst: row.tconst,
  parentTconst: row.parentTconst,
  seasonNumber: toInteger(row.seasonNumber),
  episodeNumber: toInteger(row.episodeNumber)
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleEpisode.csv' AS row 
WITH row
SKIP 5000000
CREATE (:TitleEpisode {
  tconst: row.tconst,
  parentTconst: row.parentTconst,
  seasonNumber: toInteger(row.seasonNumber),
  episodeNumber: toInteger(row.episodeNumber)
});
