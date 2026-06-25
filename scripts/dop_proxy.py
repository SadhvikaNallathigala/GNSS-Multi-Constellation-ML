import pandas as pd

df = pd.read_csv("../output/reliability_scores_v2.csv")

before = df.groupby("time")["sv"].count()

after = (
    df[df["reliability_score"] >= 70]
    .groupby("time")["sv"]
    .count()
)

print("Average Satellites Before:",
      before.mean())

print("Average Satellites After:",
      after.mean())