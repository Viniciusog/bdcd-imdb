CREATE MATERIALIZED VIEW IF NOT EXISTS episodes_view
AS SELECT tconst, parentTconst, seasonNumber, episodeNumber
FROM meu_keyspace.Episodes
WHERE tconst IS NOT NULL AND parentTconst IS NOT NULL
PRIMARY KEY (parentTconst, tconst);
