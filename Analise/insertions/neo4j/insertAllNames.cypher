CALL apoc.periodic.iterate(
LOAD CSV WITH HEADERS FROM $file AS row RETURN row,
CREATE (:ImdbName {
    nconst: row.nconst,
    primaryName: row.primaryName,
    birthYear: toInteger(row.birthYear),
    deathYear: toInteger(row.deathYear),
    primaryProfession: row.primaryProfession,
    knownForTitles: row.knownForTitles
}),
{file: 'file:///ImdbName.csv', batchSize: 1000, iterateList: true}
);
