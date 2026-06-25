import pandas as pd

df = pd.read_csv("../output/quality_features.csv")

df["label"] = 1

df.loc[df["S1C"] < 35, "label"] = 0
df.loc[df["doppler_abs"] > 2500, "label"] = 0
df.loc[df["pr_residual"] > 300000, "label"] = 0
df.loc[df["phase_residual"] > 1500000, "label"] = 0

print(df["label"].value_counts())

df.to_csv("../output/training_data.csv", index=False)

print("Saved training_data.csv")