CREATE CONSTRAINT `imp_uniq_ImdbName_nconst` IF NOT EXISTS
FOR (n: `ImdbName`)
REQUIRE (n.`nconst`) IS UNIQUE;

LOAD CSV WITH HEADERS FROM ('https://raw.githubusercontent.com/Viniciusog/bdcd-imdb/main/Analise/ImdbName.csv') AS row
WITH row
LIMIT 10000
WHERE NOT row.`nconst` IN $idsToSkip AND NOT row.`nconst` IS NULL
CALL {
  WITH row
  MERGE (n: `ImdbName` { `nconst`: row.`nconst` })
  SET n.`nconst` = row.`nconst`
  SET n.`primaryName` = row.`primaryName`
  SET n.`birthYear` = row.`birthYear`
  SET n.`deathYear` = row.`deathYear`
  SET n.`primaryProfession` = row.`primaryProfession`
  SET n.`knownForTitles` = row.`knownForTitles`
} IN TRANSACTIONS OF 10000 ROWS;


CREATE CONSTRAINT `imp_uniq_ImdbTitleAkas_titleId` IF NOT EXISTS
FOR (n: `ImdbTitleAkas`)
REQUIRE (n.`titleId`) IS UNIQUE;

LOAD CSV WITH HEADERS FROM ('https://raw.githubusercontent.com/Viniciusog/bdcd-imdb/main/Analise/ImdbTitleAkas.csv') AS row
WITH row
LIMIT 10000
WHERE NOT row.`titleId` IN $idsToSkip AND NOT row.`titleId` IS NULL
CALL {
  WITH row
  MERGE (n: `ImdbTitleAkas` { `titleId`: row.`titleId` })
  SET n.`titleId` = row.`titleId`
  SET n.`ordering` = toInteger(trim(row.`ordering`))
  SET n.`title` = row.`title`
  SET n.`region` = row.`region`
  SET n.`language` = row.`language`
  SET n.`types` = row.`types`
  SET n.`attributes` = row.`attributes`
  SET n.`isOriginalTitle` = toLower(trim(row.`isOriginalTitle`)) IN ['1','true','yes']
} IN TRANSACTIONS OF 10000 ROWS;


CREATE CONSTRAINT `imp_uniq_ImdbTitleBasics_tconst` IF NOT EXISTS
FOR (n: `ImdbTitleBasics`)
REQUIRE (n.`tconst`) IS UNIQUE;

LOAD CSV WITH HEADERS FROM ('https://raw.githubusercontent.com/Viniciusog/bdcd-imdb/main/Analise/ImdbTitleBasics.csv') AS row
WITH row
LIMIT 10000
WHERE NOT row.`tconst` IN $idsToSkip AND NOT row.`tconst` IS NULL
CALL {
  WITH row
  MERGE (n: `ImdbTitleBasics` { `tconst`: row.`tconst` })
  SET n.`tconst` = row.`tconst`
  SET n.`titleType` = row.`titleType`
  SET n.`primaryTitle` = row.`primaryTitle`
  SET n.`originalTitle` = row.`originalTitle`
  SET n.`isAdult` = toLower(trim(row.`isAdult`)) IN ['1','true','yes']
  SET n.`startYear` = toInteger(trim(row.`startYear`))
  SET n.`endYear` = row.`endYear`
  SET n.`runtimeMinutes` = row.`runtimeMinutes`
  SET n.`genres` = row.`genres`
} IN TRANSACTIONS OF 10000 ROWS;


CREATE CONSTRAINT `imp_uniq_ImdbTitleCrew_tconst` IF NOT EXISTS
FOR (n: `ImdbTitleCrew`)
REQUIRE (n.`tconst`) IS UNIQUE;

LOAD CSV WITH HEADERS FROM ('https://raw.githubusercontent.com/Viniciusog/bdcd-imdb/main/Analise/ImdbTitleCrew.csv') AS row
WITH row
LIMIT 10000
WHERE NOT row.`tconst` IN $idsToSkip AND NOT row.`tconst` IS NULL
CALL {
  WITH row
  MERGE (n: `ImdbTitleCrew` { `tconst`: row.`tconst` })
  SET n.`tconst` = row.`tconst`
  SET n.`directors` = row.`directors`
  SET n.`writers` = row.`writers`
} IN TRANSACTIONS OF 10000 ROWS;


CREATE CONSTRAINT `imp_uniq_ImdbTitlePrincipals_tconst` IF NOT EXISTS
FOR (n: `ImdbTitlePrincipals`)
REQUIRE (n.`tconst`) IS UNIQUE;

LOAD CSV WITH HEADERS FROM ('https://raw.githubusercontent.com/Viniciusog/bdcd-imdb/main/Analise/ImdbTitlePrincipals.csv') AS row
WITH row
LIMIT 10000
WHERE NOT row.`tconst` IN $idsToSkip AND NOT row.`tconst` IS NULL
CALL {
  WITH row
  MERGE (n: `ImdbTitlePrincipals` { `tconst`: row.`tconst` })
  SET n.`tconst` = row.`tconst`
  SET n.`ordering` = toInteger(trim(row.`ordering`))
  SET n.`nconst` = row.`nconst`
  SET n.`category` = row.`category`
  SET n.`job` = row.`job`
  SET n.`characters` = row.`characters`
} IN TRANSACTIONS OF 10000 ROWS;


CREATE CONSTRAINT `imp_uniq_ImdbTitleRatings_tconst` IF NOT EXISTS
FOR (n: `ImdbTitleRatings`)
REQUIRE (n.`tconst`) IS UNIQUE;

LOAD CSV WITH HEADERS FROM ('https://raw.githubusercontent.com/Viniciusog/bdcd-imdb/main/Analise/ImdbTitleRatings.csv') AS row
WITH row
LIMIT 10000
WHERE NOT row.`tconst` IN $idsToSkip AND NOT row.`tconst` IS NULL
CALL {
  WITH row
  MERGE (n: `ImdbTitleRatings` { `tconst`: row.`tconst` })
  SET n.`tconst` = row.`tconst`
  SET n.`averageRating` = toFloat(trim(row.`averageRating`))
  SET n.`numVotes` = toInteger(trim(row.`numVotes`))
} IN TRANSACTIONS OF 10000 ROWS;
