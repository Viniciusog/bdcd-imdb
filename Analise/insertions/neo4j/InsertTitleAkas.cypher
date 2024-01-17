LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleAkas.csv' AS row 
WITH row
SKIP 0 LIMIT 1000000
CREATE (:TitleAka {
  titleId: row.titleId,
  ordering: toInteger(row.ordering),
  title: row.title,
  region: row.region,
  language: row.language,
  types: row.types,
  attributes: row.attributes,
  isOriginalTitle: toInteger(row.isOriginalTItle)
});

LOAD CSV WITH HEADERS FROM 'file:///ImdbTitleAkas.csv' AS row 
WITH row
SKIP 1000000
CREATE (:TitleAka {
  titleId: row.titleId,
  ordering: toInteger(row.ordering),
  title: row.title,
  region: row.region,
  language: row.language,
  types: row.types,
  attributes: row.attributes,
  isOriginalTitle: toInteger(row.isOriginalTItle)
});