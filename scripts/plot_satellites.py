import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/results_summary.csv")

plt.figure(figsize=(8,5))

plt.bar(
    df["Dataset"],
    df["Satellites"]
)

plt.ylabel("Number of Satellites")
plt.title("Satellite Availability")

plt.tight_layout()

plt.savefig("output/satellite_count.png")

plt.show()