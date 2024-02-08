import pandas as pd

dfTitleBasic = pd.read_csv("../Analise/ImdbTitleEpisode.csv", nrows=10000)

dfTitleBasic.info()

dfTitleBasic.to_csv("ImdbTitleEpisode10k.csv", index=False)