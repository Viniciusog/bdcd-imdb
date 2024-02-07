import pandas as pd

def filter1000ep():
    dfTitle = pd.read_csv("../Analise/ImdbTitleEpisode.csv", nrows=10000)




    dfTitle.to_csv("ImdbTitleEpisode10000.csv", index=False)


filter1000ep()
