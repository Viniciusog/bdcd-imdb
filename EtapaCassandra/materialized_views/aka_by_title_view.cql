CREATE MATERIALIZED VIEW IF NOT EXISTS aka_by_title_view
AS SELECT titleId, ordering, title, region, language, types, attributes, isOriginalTitle
FROM your_keyspace.AkaByTitle
WHERE titleId IS NOT NULL AND ordering IS NOT NULL
PRIMARY KEY (titleId, ordering);
