import pandas as pd

# Leitura dos arquivos
title_basic = pd.read_csv('../Analise/ImdbTitleBasicsWithRating.csv', nrows=10000)
title_crew = pd.read_csv('../Analise/ImdbTitleCrew.csv')
title_crew.rename(columns={'tconst': 'tconstTitle'}, inplace=True)

# Merge dos Diretores
title_by_director = pd.merge(title_basic, title_crew[['tconstTitle','directors']], left_on="tconst", right_on="tconstTitle", how='left')

df_formatado = pd.DataFrame(columns=title_basic.columns)

# Loop sobre as linhas do DataFrame original
for index, row in title_by_director.iterrows():
    directors = row['directors'].split(',')  # Divide os diretores em uma lista
    for director in directors:
        nova_linha = row.copy()  # Converta a linha para um dicionário
        nova_linha['director'] = director.strip()  # Remove espaços em branco
        df_formatado = pd.concat([df_formatado, nova_linha.to_frame().T],ignore_index=True) 

df_formatado = df_formatado.drop(columns=['tconstTitle'])

# Exibe informações sobre o DataFrame resultante
df_formatado.info()

# Salva o DataFrame em um arquivo CSV
df_formatado.to_csv("ImdbTitleBasicsDirectorRelation.csv", index=False)
