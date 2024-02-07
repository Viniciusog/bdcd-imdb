import pandas as pd

names = pd.read_csv("../Analise/ImdbName.csv", nrows=10000)

names.to_csv("ImdbName10k.csv", index=False)