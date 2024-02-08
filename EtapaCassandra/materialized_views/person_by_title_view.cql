CREATE MATERIALIZED VIEW IF NOT EXISTS person_by_title_view
AS SELECT tconst, nconst, category, characters, primaryName, birthYear, deathYear, primaryProfession
FROM meu_keyspace.PersonByTitle
WHERE tconst IS NOT NULL AND nconst IS NOT NULL
PRIMARY KEY (tconst, nconst);
