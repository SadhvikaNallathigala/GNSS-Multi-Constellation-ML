import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "output/gnss_dataset_v2.csv",
    low_memory=False
)

plt.figure(figsize=(10,6))

for label,name in zip(
    [0,1,2],
    ["Open Sky","Metal","Foil"]
):
    subset = df[df["label"]==label]

    plt.hist(
        subset["snr"],
        bins=40,
        alpha=0.5,
        label=name
    )

plt.xlabel("SNR (dB)")
plt.ylabel("Count")
plt.title("SNR Distribution by Environment")

plt.legend()

plt.tight_layout()

plt.savefig(
    "output/snr_distribution.png",
    dpi=300
)

print("Saved output/snr_distribution.png")

plt.show()