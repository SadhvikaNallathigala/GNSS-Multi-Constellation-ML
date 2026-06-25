import pandas as pd

df = pd.read_csv("../output/quality_features.csv")

df["quality_score"] = (
    0.5 * df["snr_norm"]
    + 0.25 * (1 - df["doppler_abs"] / df["doppler_abs"].max())
    + 0.25 * (1 - df["pr_residual"] / df["pr_residual"].max())
)

df["quality_score"] *= 100

df.to_csv(
    "../output/satellite_quality.csv",
    index=False
)

print(df[["sv", "quality_score"]].head())

print("\nAverage Score:")
print(df["quality_score"].mean())