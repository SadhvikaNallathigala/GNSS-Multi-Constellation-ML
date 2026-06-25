import pandas as pd

df = pd.read_csv("../output/gnss_dataset.csv")

print(df["label"].value_counts())
print(df["label"].unique())