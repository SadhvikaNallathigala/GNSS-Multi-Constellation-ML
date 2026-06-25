# scripts/check_dataset_classes.py

import pandas as pd

df = pd.read_csv("output/gnss_dataset_v2.csv")

print(df.columns)

print("\nUnique Labels:")
print(df["label"].unique())

print("\nCounts:")
print(df["label"].value_counts())