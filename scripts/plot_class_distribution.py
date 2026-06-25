import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "output/gnss_dataset_v2.csv",
    low_memory=False
)

counts = df["label"].value_counts().sort_index()

labels = [
    "Open Sky",
    "Metal",
    "Foil"
]

plt.figure(figsize=(8,5))

plt.bar(labels, counts.values)

plt.ylabel("Samples")
plt.title("Dataset Class Distribution")

plt.tight_layout()

plt.savefig(
    "output/class_distribution.png",
    dpi=300
)

print("Saved output/class_distribution.png")

plt.show()