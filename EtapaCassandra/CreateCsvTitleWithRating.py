import pandas as pd

# Relaciona os 10k primeiros títulos com suas respectivas avaliações para ser inserido no cassandra
def insertRating():
    dfTitle = pd.read_csv("../Analise/ImdbTitleBasics.csv", nrows=10000)
    dfRating = pd.read_csv("../Analise/ImdbTitleRatings.csv")

    dfMerged = pd.merge(
        dfTitle, dfRating[["tconst", "averageRating"]], on="tconst", how="left"
    )

    # dfMerged["averageRating"].fillna(0, inplace=True)

    # print(dfRating['tconst'].nunique())-1, 
    # print(dfRating["tconst"].nunique())
    
    dfMerged.info()


    # Supondo que 'df' seja o seu DataFrame
    # Salvar o DataFrame em um arquivo CSV chamado 'nome_do_arquivo.csv'
    dfMerged.to_csv("ImdbTitleBasicsWithRating.csv", index=False)


insertRating()
