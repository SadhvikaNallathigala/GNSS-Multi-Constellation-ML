import pandas as pd
import os

os.makedirs("output", exist_ok=True)

results = pd.DataFrame({
    "Dataset": [
        "Metal Plate",
        "Foil",
        "Foil02",
        "SKY01"
    ],
    "Satellites": [
        60,
        40,
        42,
        69
    ],
    "Position_Error_m": [
        3.9683,
        11.3532,
        5.7269,
        0.0
    ],
    "Mean_SNR": [
        0,
        0,
        0,
        45.20
    ]
})

print(results)

results.to_csv(
    "output/results_summary.csv",
    index=False
)

print("\nSaved output/results_summary.csv")