import pandas as pd

# Carregar os DataFrames
principal = pd.read_csv('../Analise/ImdbTitlePrincipals.csv')
names = pd.read_csv('../Analise/ImdbName.csv')

# Remover colunas desnecessárias
principal = principal.drop(['ordering', 'job'], axis=1)
names = names.drop(['knownForTitles'], axis=1)

# Fazer o merge dos DataFrames
principal_complete = pd.merge(principal, names[['nconst','primaryName','birthYear','deathYear','primaryProfession']], on='nconst', how='left')

# Substituir vírgulas por pontos na coluna 'characters'
principal_complete['characters'] = principal_complete['characters'].str.replace(',', '.', regex=False)

# Mostrar informações do DataFrame modificado
principal_complete.info()

# Salvar para CSV
principal_complete.to_csv("ImdbTitlePersonByTitleRelation.csv", index=False)



""" principal = pd.read_csv('../Analise/ImdbTitlePrincipals.csv')
names = pd.read_csv('../Analise/ImdbName.csv')

principal = principal.drop(['ordering', 'job'], axis=1)
names = names.drop(['knownForTitles'], axis=1)

principal_complete = pd.merge(principal, names[['nconst','primaryName','birthYear','deathYear','primaryProfession']], on='nconst', how='left')

principal_complete.info()

principal_complete.to_csv("ImdbTitlePersonByTitleRelation.csv", index=False)
 """