# ----- IMPORTAÇÃO DOS DADOS -----
```js
LOAD CSV WITH HEADERS FROM 'file:#/ImdbTitleAkas.csv' AS row 
WITH row
LIMIT 10000
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
```

```js
LOAD CSV WITH HEADERS FROM 'file:#/ImdbTitleRatings.csv' AS row
WITH row 
SKIP 0 LIMIT 10000
CREATE (:TitleRatings {
    tconst: row.tconst,
    averageRating: toFloat(row.averageRating),
    numVotes: toInteger(row.numVotes)
});
```

```js
LOAD CSV WITH HEADERS FROM 'file:#/ImdbTitlePrincipals.csv' AS row
WITH row 
SKIP 0 LIMIT 10000
CREATE (:TitlePrincipal {
    tconst: row.tconst,
    ordering: toInteger(row.ordering),
    nconst: row.nconst,
    category: row.category,
    job: row.job,
    characters: row.characters
});
```

```js
LOAD CSV WITH HEADERS FROM 'file:#/ImdbTitleEpisode.csv' AS row 
WITH row
SKIP 0 LIMIT 10000
CREATE (:TitleEpisode {
  tconst: row.tconst,
  parentTconst: row.parentTconst,
  seasonNumber: toInteger(row.seasonNumber),
  episodeNumber: toInteger(row.episodeNumber)
});
```

```js
LOAD CSV WITH HEADERS FROM 'file:#/ImdbTitleCrew.csv' AS row 
WITH row
SKIP 0 LIMIT 10000
CREATE (:TitleCrew {
  tconst: row.tconst,
  directors: row.directors,
  writers: row.writers
});
```

```js
LOAD CSV WITH HEADERS FROM 'file:#/ImdbTitleBasics.csv' AS row
WITH row 
SKIP 0 LIMIT 10000
CREATE (:TitleBasics {
    tconst: row.tconst,
    titleType: row.titleType,
    primaryTitle: row.primaryTitle,
    originalTitle: row.originalTitle,
    isAdult: toInteger(row.isAdult),
    startYear: toInteger(row.startYear),
    runtimeMinutes: toInteger(row.runtimeMinutes),
    genres: row.genres
});
```

```js
LOAD CSV WITH HEADERS FROM 'file:#/ImdbName.csv' AS row
WITH row 
SKIP 0 LIMIT 10000
CREATE (:ImdbNameL {
    nconst: row.nconst,
    primaryName: row.primaryName,
    birthYear: toInteger(row.birthYear),
    deathYear: toInteger(row.deathYear),
    primaryProfession: row.primaryProfession,
    knownForTitles: row.knownForTitles
});
```


# ----- CRIAÇÃO DAS RELAÇÕES -------

# Name --> Principal
```js
MATCH (p:ImdbNameL), (principal:TitlePrincipal)
WHERE p.nconst = principal.nconst
MERGE (p)-[:TRABALHOU_COMO]->(principal)
```

# Principal --> Name
```js
MATCH (p:ImdbNameL), (principal:TitlePrincipal)
WHERE p.nconst = principal.nconst
MERGE (principal)-[:DESEMPENHADO_POR]->(p)
```

# Person --> PrimaryProfession - Cria os nós PrimaryProfession
```js
MATCH (p:ImdbNameL)
WITH p, split(p.primaryProfession, ",") AS valores
UNWIND valores AS valor
MERGE (primaryp:PrimaryProfession {description: valor})
MERGE (p)-[r:TRABALHA_COMO]->(primaryp)
```

# TitleBasics -> TitleGenre
# Cria os nós TitleGenre
```js
MATCH (t:TitleBasics)
WITH t, split(t.genres, ",") AS generos
UNWIND generos AS genero
MERGE (tg:TitleGenres {description: genero})
MERGE (t)-[r:EH_DO_GENERO]->(tg)
```

# TitleGenre -> TitleBasics
```js
MATCH (t:TitleBasics)
WITH t, split(t.genres, ",") AS generos
UNWIND generos AS genero
MERGE (tg:TitleGenres {description: genero})
MERGE (tg)-[r:INCLUI_O_TITULO]->(t)
```

# TitleBasics -> TitleRatings
```js
MATCH (n:TitleBasics), (m:TitleRatings)
WHERE n.tconst = m.tconst
MERGE (n)-[:AVALIADO_EM]->(m)
MERGE (m)-[:AVALIA]->(n);
```



# TitleBasics -> TitlePrincipals
```js
MATCH (n:TitleBasics), (m:TitlePrincipals)
WHERE n.tconst = m.tconst
MERGE (n)-[:CONTOU_COM]->(m)
MERGE (m)-[:TRABALHOU_EM]->(n);
```

# TitleBasics -> TitleEpisodes
```js
MATCH (n:TitleBasics), (m:TitleEpisode)
WHERE n.tconst = m.parentTconst
MERGE (n)-[:APRESENTA]->(m)
MERGE (m)-[:FAZ_PARTE_DE]->(n);
```

# TitleAka -> TitleBasics
```js
MATCH (aka:ImdbTitleAka), (basic:ImdbTitleBasic)
WHERE aka.titleId = basic.tconst
MERGE (aka)-[:ALSO_KNOWN_AS]->(basic);
```

# Inserção de filmes para episódios
```js
WITH [
    'tt0041038', 'tt0989125', 'tt0040051', 
    'tt0959862', 'tt0044243', 'tt0044284', 
    'tt0341798', 'tt0914702', 'tt0047745', 
    'tt0046637', 'tt0047768', 'tt0047702', 
    'tt0046587', 'tt0046593', 'tt0050013', 
    'tt0048893', 'tt4280482', 'tt0161126', 
    'tt0453991', 'tt0441950', 'tt0793361'
] AS tconstsList
LOAD CSV WITH HEADERS FROM 'file:#/ImdbTitleBasics.csv' AS row
WITH row
WHERE row.tconst IN tconstsList
CREATE (:TitleBasics {
    tconst: row.tconst,
    titleType: row.titleType,
    primaryTitle: row.primaryTitle,
    originalTitle: row.originalTitle,
    isAdult: row.isAdult,
    startYear: row.startYear,
    endYear: row.endYear,
    runtimeMinutes: row.runtimeMinutes,
    genres: row.genres
})
```

# ---- CONSULTAS -----

# Retorna obra com título "Blacksmith Scene"
MATCH (title:TitleBasics)
WHERE title.primaryTitle CONTAINS 'Blacksmith Scene'
RETURN title

# Retorna tipo da obra com título Broadway Television Theatre
MATCH (title:TitleBasics {primaryTitle: 'Broadway Television Theatre'})
RETURN title.titleType

# Retorna os filmes que foram lançados antes de 2022 e não tiveram termino ou que tiveram
# término depois de 2020
MATCH (title:TitleBasics)
WHERE title.startYear <= 2022 AND (title.endYear IS NULL OR title.endYear >= 2020)
RETURN title

# Filtra os títulos que possuem avaliação média entre 7 e 9
MATCH (title:TitleBasics)-[:AVALIADO_EM]->(rating:TitleRatings)
WHERE rating.averageRating >= 7.0 AND rating.averageRating <= 9.0
RETURN title, rating

# Filtra as pessoas que contém nome com a palavra "John"
MATCH (person:ImdbName)
WHERE person.primaryName CONTAINS 'John'
RETURN person

# Retorna todas as pessoas que atuam como editor(a) 
MATCH (p:ImdbNameL)-[:TRABALHA_COMO]->(primaryProfession:PrimaryProfession)
WHERE primaryProfession.description = "editor"
RETURN p, primaryProfession

# Retorna todos os títulos que são do gênero "Romance"
MATCH (p:TitleBasics)-[:EH_DO_GENERO]->(g:TitleGenres)
WHERE g.description = "Romance"
RETURN p, g limit 10