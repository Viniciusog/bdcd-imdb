CREATE MATERIALIZED VIEW IF NOT EXISTS episodes_by_title_view
AS SELECT tconst, parentTconst, seasonNumber, episodeNumber
FROM meu_keyspace.EpisodesByTitle
WHERE tconst IS NOT NULL AND parentTconst IS NOT NULL
PRIMARY KEY (tconst, parentTconst);
