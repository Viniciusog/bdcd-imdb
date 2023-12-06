def get_all_genres():
    with open("./ImdbTitleBasics.csv", 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)

        print("get_all_genres ....")

        allGenres = []

        for linha in leitor_csv:
            for key, value in linha.items():
                if key == 'genres':  
                    myValue = value.split(',')

                    for myGenre in myValue:
                        if myGenre not in allGenres:
                            allGenres.append(myGenre)            
        
        allGenres.remove("\\N")
        print(allGenres)
        return allGenres