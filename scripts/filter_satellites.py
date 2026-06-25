import pandas as pd

df = pd.read_csv("../output/satellite_quality.csv")

before = df["sv"].nunique()

filtered = df[df["quality_score"] >= 70]

after = filtered["sv"].nunique()

print("Satellites Before :", before)
print("Satellites After  :", after)

print("\nRemoved Satellites:")

removed = set(df["sv"].unique()) - set(filtered["sv"].unique())

print(sorted(list(removed)))

filtered.to_csv(
    "../output/high_quality_satellites.csv",
    index=False
)