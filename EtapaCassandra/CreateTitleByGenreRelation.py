import pandas as pd

def insertTitleAkaRelation():
    dfTitle = pd.read_csv("../Analise/ImdbTitleBasicsWithRating.csv", nrows=10000)
    
    dfTitle.info()
    
    # Supondo que 'df' seja o seu DataFrame

    # Dividir os gêneros em cada linha usando a vírgula como delimitador
    generos_divididos = dfTitle['generos'].str.split(',')

    # Converter a lista de gêneros em um conjunto para eliminar duplicatas
    generos_unicos = set([genero.strip() for sublist in generos_divididos.dropna() for genero in sublist])

    # Calcular o tamanho do conjunto para obter o número total de gêneros únicos
    quantidade_generos_diferentes = len(generos_unicos)

    print("Quantidade total de gêneros diferentes:", quantidade_generos_diferentes)




    # Supondo que 'df' seja o seu DataFrame
    # Salvar o DataFrame em um arquivo CSV chamado 'nome_do_arquivo.csv'
    # dfMerged.to_csv("ImdbTitleBasicsAkaRelation.csv", index=False)


insertTitleAkaRelation()
