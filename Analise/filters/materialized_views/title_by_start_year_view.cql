CREATE MATERIALIZED VIEW IF NOT EXISTS title_by_start_year_view
AS SELECT tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating
FROM your_keyspace.TitleByStartYear
WHERE tconst IS NOT NULL AND startYear IS NOT NULL
PRIMARY KEY (startYear, tconst);