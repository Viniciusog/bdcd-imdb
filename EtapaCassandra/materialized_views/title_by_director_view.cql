CREATE MATERIALIZED VIEW IF NOT EXISTS title_by_director_view
AS SELECT tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating, directors, director
FROM your_keyspace.TitleByDirector
WHERE tconst IS NOT NULL AND director IS NOT NULL
PRIMARY KEY (director, tconst);