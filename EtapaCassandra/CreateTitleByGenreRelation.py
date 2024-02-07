import pandas as pd

def insertTitleGenreRelation():
    df_original = pd.read_csv("../Analise/ImdbTitleBasicsWithRating.csv", nrows=10000)
        
    # DataFrame vazio para armazenar os dados separados por gênero
    df_por_genero = pd.DataFrame(columns=df_original.columns)

    # Loop sobre as linhas do DataFrame original
    for index, row in df_original.iterrows():
        generos = row['genres'].split(',')  # Divide os gêneros em uma lista
        
        # Para cada gênero na lista de gêneros
        for genero in generos:
            # Cria uma cópia dos dados da linha
            nova_linha = row.copy()
            # Define o gênero da nova linha como o gênero atual do loop
            nova_linha['genre'] = genero.strip()  # Remove espaços em branco
            # Adiciona a nova linha ao DataFrame df_por_genero
            df_por_genero = pd.concat([df_por_genero, nova_linha.to_frame().T], ignore_index=True)

    # Exibe o novo DataFrame com os dados separados por gênero
    df_por_genero.info()
    print(df_por_genero)
    
    df_por_genero.to_csv("ImdbTitleBasicsGenreRelation.csv", index=False)
    
    


insertTitleGenreRelation()
