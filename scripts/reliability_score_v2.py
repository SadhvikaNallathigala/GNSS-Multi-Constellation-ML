import pandas as pd

df = pd.read_csv("../output/training_data.csv")

score = (
    40 * df["snr_norm"] +
    20 * (1 - df["doppler_abs"]/df["doppler_abs"].max()) +
    20 * (1 - df["pr_residual"]/df["pr_residual"].max()) +
    20 * (1 - df["phase_residual"]/df["phase_residual"].max())
)

df["reliability_score"] = score.clip(0,100)

print(df[[
    "sv",
    "reliability_score"
]].head())

print("\nAverage Reliability:")
print(df["reliability_score"].mean())

df.to_csv("../output/reliability_scores_v2.csv", index=False)