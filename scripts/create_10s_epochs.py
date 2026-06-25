import pandas as pd

df = pd.read_csv(
    "output/gnss_dataset_v2.csv",
    low_memory=False
)

df["time"] = pd.to_datetime(df["time"])

# 10-second epochs
df["epoch_30s"] = df["time"].dt.floor("30s")

epoch_features = (
    df.groupby(["epoch_30s", "label"])
      .agg(
          mean_snr=("snr", "mean"),
          std_snr=("snr", "std"),
          sat_count=("sv", "nunique")
      )
      .reset_index()
)

print(epoch_features.head())

epoch_features.to_csv(
    "output/gnss_dataset_30s.csv",
    index=False
)

print("Saved output/gnss_dataset_30s.csv")