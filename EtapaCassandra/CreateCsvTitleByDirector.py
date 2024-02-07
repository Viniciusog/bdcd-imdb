import pandas as pd

#Leitura dos arquivos
title_basic = pd.read_csv('https://raw.githubusercontent.com/Viniciusog/bdcd-imdb/main/Analise/ImdbTitleBasicsWithRating.csv',  error_bad_lines=False, nrows=10000)

title_crew = pd.read_csv('https://raw.githubusercontent.com/Viniciusog/bdcd-imdb/main/Analise/ImdbTitleCrew.csv',  error_bad_lines=False, nrows=10000)

#Merge dos Diretores
title_by_director = title_basic.merge(title_crew[['tconst', 'directors']], on='tconst', how='inner')

title_by_director.rename(columns={'directors': 'nconst'}, inplace=True)

#Criação do CSV
title_by_director.to_csv('title_by_director.csv', index=False)