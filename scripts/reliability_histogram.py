import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/reliability_scores_v2.csv")

plt.figure(figsize=(8,5))

plt.hist(
    df["reliability_score"],
    bins=30
)

plt.title("Reliability Score Distribution")
plt.xlabel("Reliability Score")
plt.ylabel("Count")

plt.grid(True)

plt.savefig(
    "output/reliability_distribution.png",
    dpi=300
)

plt.show()