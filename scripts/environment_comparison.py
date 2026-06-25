import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Dataset": [
        "SKY01",
        "Metal Plate",
        "Foil02",
        "Foil"
    ],
    "Position_Error":[
        0,
        3.9683,
        5.7269,
        11.3532
    ]
})

plt.figure(figsize=(8,5))

plt.bar(
    df["Dataset"],
    df["Position_Error"]
)

plt.title("Position Error Comparison")
plt.ylabel("Error (m)")

plt.savefig(
    "output/environment_comparison.png",
    dpi=300
)

plt.show()