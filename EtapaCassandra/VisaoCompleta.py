from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])  # COLOCA O IP DO SEU CASSANDRA AQUI
session = cluster.connect('meu_keyspace')  # COLOCAR O NOME DO SEU KEYSPACE AQUI

# Define a function to create the consolidated_data table
def create_consolidated_table():
    session.execute("""
        CREATE TABLE consolidated_data (
        titleId text,
        ordering text,
        title text,
        region text,
        language text,
        types text,
        attributes text,
        isOriginalTitle boolean,
        tconst text,
        titleType text,
        primaryTitle text,
        originalTitle text,
        isAdult boolean,
        startYear int,
        endYear text,
        runtimeMinutes int,
        genres text,
        averageRating float,
        genre text,
        parentTconst text,
        seasonNumber text,
        episodeNumber text,
        directors text,
        director text,
        nconst text,
        category text,
        characters text,
        primaryName text,
        birthYear text,
        deathYear text,
        primaryProfession text,
        knownForTitles text,
        PRIMARY KEY ((titleId, ordering), tconst, parentTconst, director, nconst, startYear)
);

    """)

# Define a function to consolidate data
def consolidate_data():
    rows = session.execute('SELECT * FROM AkaByTitle')
    for row in rows:
        tconst = row.titleid
        ordering = row.ordering
        title = row.title
        region = row.region
        language = row.language
        types = row.types
        attributes = row.attributes
        isOriginalTitle = row.isoriginaltitle

        # Insert data into the consolidated table
        session.execute(
            """
            INSERT INTO consolidated_data (titleId, ordering, title, region, language, types, attributes, isOriginalTitle)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (tconst, ordering, title, region, language, types, attributes, isOriginalTitle)
        )

    # Retrieve data from the TitleByGenre table
    rows = session.execute('SELECT * FROM TitleByGenre')
    for row in rows:
        tconst = row.tconst
        titleType = row.titletype
        primaryTitle = row.primarytitle
        originalTitle = row.originaltitle
        isAdult = row.isadult
        startYear = row.startyear
        endYear = row.endyear
        runtimeMinutes = row.runtimeminutes
        genres = row.genres
        averageRating = row.averagerating
        genre = row.genre

        # Insert data into the consolidated table
        session.execute(
            """
            INSERT INTO consolidated_data (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating, genre)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating, genre)
        )

    # Retrieve data from the episodes_by_title table
    rows = session.execute('SELECT * FROM episodes_by_title')
    for row in rows:
        tconst = row.tconst
        parenttconst = row.parenttconst
        seasonnumber = row.seasonnumber
        episodenumber = row.episodenumber

        # Insert data into the consolidated table
        session.execute(
            """
            INSERT INTO consolidated_data (tconst, parentTconst, seasonNumber, episodeNumber)
            VALUES (%s, %s, %s, %s)
            """,
            (tconst, parenttconst, seasonnumber, episodenumber)
        )

    # Retrieve data from the title_by_director table
    rows = session.execute('SELECT * FROM title_by_director')
    for row in rows:
        tconst = row.tconst
        titletype = row.titletype
        primarytitle = row.primarytitle
        originaltitle = row.originaltitle
        isadult = row.isadult
        startyear = row.startyear
        endyear = row.endyear
        runtimeminutes = row.runtimeminutes
        genres = row.genres
        averagerating = row.averagerating
        directors = row.directors
        director = row.director

        # Insert data into the consolidated table
        session.execute(
            """
            INSERT INTO consolidated_data (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating, directors, director)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (tconst, titletype, primarytitle, originaltitle, isadult, startyear, endyear, runtimeminutes, genres, averagerating, directors, director)
        )

    # Retrieve data from the person_by_title table
    rows = session.execute('SELECT * FROM person_by_title')
    for row in rows:
        tconst = row.tconst
        nconst = row.nconst
        category = row.category
        characters = row.characters
        primaryname = row.primaryname
        birthyear = row.birthyear
        deathyear = row.deathyear
        primaryprofession = row.primaryprofession

        # Insert data into the consolidated table
        session.execute(
            """
            INSERT INTO consolidated_data (tconst, nconst, category, characters, primaryName, birthYear, deathYear, primaryProfession)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (tconst, nconst, category, characters, primaryname, birthyear, deathyear, primaryprofession)
        )

    # Retrieve data from the person table
    rows = session.execute('SELECT * FROM person')
    for row in rows:
        nconst = row.nconst
        primaryname = row.primaryname
        birthyear = row.birthyear
        deathyear = row.deathyear
        primaryprofession = row.primaryprofession
        knownfortitles = row.knownfortitles

        # Insert data into the consolidated table
        session.execute(
            """
            INSERT INTO consolidated_data (nconst, primaryName, birthYear, deathYear, primaryProfession, knownForTitles)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (nconst, primaryname, birthyear, deathyear, primaryprofession, knownfortitles)
        )

    # Retrieve data from the title_by_start_year table
    rows = session.execute('SELECT * FROM title_by_start_year')
    for row in rows:
        tconst = row.tconst
        titletype = row.titletype
        primarytitle = row.primarytitle
        originaltitle = row.originaltitle
        isadult = row.isadult
        startyear = row.startyear
        endyear = row.endYear
        runtimeminutes = row.runtimeminutes
        genres = row.genres
        averagerating = row.averagerating

        # Insert data into the consolidated table
        session.execute(
            """
            INSERT INTO consolidated_data (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (tconst, titletype, primarytitle, originaltitle, isadult, startyear, endyear, runtimeminutes, genres, averagerating)
        )

    # Retrieve data from the episodes table
    rows = session.execute('SELECT * FROM episodes')
    for row in rows:
        tconst = row.tconst
        parenttconst = row.parenttconst
        seasonnumber = row.seasonnumber
        episodenumber = row.episodenumber

        # Insert data into the consolidated table
        session.execute(
            """
            INSERT INTO consolidated_data (tconst, parentTconst, seasonNumber, episodeNumber)
            VALUES (%s, %s, %s, %s)
            """,
            (tconst, parenttconst, seasonnumber, episodenumber)
        )

# Create the consolidated_data table
# create_consolidated_table()

# Call the function to consolidate data
consolidate_data()

# Close the connection
cluster.shutdown()