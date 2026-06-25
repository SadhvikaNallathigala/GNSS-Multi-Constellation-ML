import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "output/gnss_dataset_v2.csv",
    low_memory=False
)

counts = df["constellation"].value_counts()

plt.figure(figsize=(8,5))

counts.plot(kind="bar")

plt.ylabel("Observations")
plt.xlabel("Constellation")
plt.title("GNSS Constellation Distribution")

plt.tight_layout()

plt.savefig(
    "output/constellation_distribution.png",
    dpi=300
)

print("Saved output/constellation_distribution.png")

plt.show()