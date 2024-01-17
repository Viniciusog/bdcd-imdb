CALL apoc.periodic.iterate(
  'LOAD CSV WITH HEADERS FROM $file AS row RETURN row',
  'CREATE (:ImdbName {
    tconst: row.tconst,
    parentTconst: row.parentTconst,
    seasonNumber: toInteger(row.seasonNumber),
    episodeNumber: toInteger(row.episodeNumber)
  })',
  {file: 'file:///ImdbTitleEpisode.csv', batchSize: 1000, iterateList: true}
);
