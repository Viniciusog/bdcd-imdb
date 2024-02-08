CREATE MATERIALIZED VIEW IF NOT EXISTS title_by_genre_view
AS SELECT tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating, genre
FROM meu_keyspace.TitleByGenre
WHERE tconst IS NOT NULL AND genre IS NOT NULL
PRIMARY KEY (tconst, genre);
