import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/reliability_scores_v2.csv")

top = (
    df.groupby("sv")["reliability_score"]
      .mean()
      .sort_values(ascending=False)
      .head(15)
)

plt.figure(figsize=(10,6))

top.plot(kind="bar")

plt.title("Top 15 Satellites by Reliability")
plt.ylabel("Mean Reliability Score")

plt.tight_layout()

plt.savefig(
    "output/top_satellites.png",
    dpi=300
)

plt.show()