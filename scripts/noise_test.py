import pandas as pd
import numpy as np

df = pd.read_csv("output/gnss_dataset_v2.csv")

noise = np.random.normal(
    0,
    3,
    size=len(df)
)

df["snr"] = df["snr"] + noise

df.to_csv(
    "output/gnss_dataset_noisy.csv",
    index=False
)

print("Noisy dataset saved")