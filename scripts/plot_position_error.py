import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/results_summary.csv")

plt.figure(figsize=(8,5))

plt.bar(
    df["Dataset"],
    df["Position_Error_m"]
)

plt.ylabel("Position Error (m)")
plt.title("Position Error Comparison")

plt.tight_layout()

plt.savefig("output/position_error.png")

plt.show()