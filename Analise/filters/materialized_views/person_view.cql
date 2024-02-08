CREATE MATERIALIZED VIEW IF NOT EXISTS person_view
AS SELECT nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles
FROM your_keyspace.Person
WHERE nconst IS NOT NULL
PRIMARY KEY (nconst);