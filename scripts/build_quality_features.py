import pandas as pd

df = pd.read_csv("../output/raw_observations.csv")

df["snr_norm"] = df["S1C"] / df["S1C"].max()

df["doppler_abs"] = abs(df["D1C"])

df["pr_residual"] = abs(
    df["C1C"] - df.groupby("sv")["C1C"].transform("mean")
)

df["phase_residual"] = abs(
    df["L1C"] - df.groupby("sv")["L1C"].transform("mean")
)

features = df[
    [
        "time",
        "sv",
        "S1C",
        "C1C",
        "L1C",
        "D1C",
        "snr_norm",
        "doppler_abs",
        "pr_residual",
        "phase_residual"
    ]
]

features.to_csv(
    "../output/quality_features.csv",
    index=False
)

print(features.head())
print("\nRows:", len(features))