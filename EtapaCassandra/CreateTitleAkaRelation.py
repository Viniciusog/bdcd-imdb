import pandas as pd

# Pega os Aka's que estejam relacionados com os 10k primeiros títulos
def insertTitleAkaRelation():
    dfTitle = pd.read_csv("../Analise/ImdbTitleBasicsWithRating.csv", nrows=10000)
    dfAka = pd.read_csv("../Analise/ImdbTitleAkas.csv")

    dfMerged = pd.merge(
        dfAka, dfTitle[["tconst"]],
        left_on="titleId", right_on="tconst",
        how="left"
    )
    
    # Remover linhas onde o valor da coluna 'tconst' é vazio
    # Ou seja, vamos manter apenas os Akas que estão relacionadas aos 10k primeiros títulos
    dfMerged = dfMerged.dropna(subset=['tconst'])

    # Remover a coluna 'nome_da_coluna' do DataFrame
    dfMerged = dfMerged.drop(columns=['tconst'])

    # print(dfRating['tconst'].nunique())-1, 
    # print(dfRating["tconst"].nunique())
    
    dfMerged.info()


    # Supondo que 'df' seja o seu DataFrame
    # Salvar o DataFrame em um arquivo CSV chamado 'nome_do_arquivo.csv'
    dfMerged.to_csv("ImdbTitleBasicsAkaRelation.csv", index=False)


insertTitleAkaRelation()
