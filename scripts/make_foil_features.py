import georinex as gr
import pandas as pd

obs = gr.load("../data/sadhvika_foil.26o")

snr = obs["S1C"].to_dataframe().reset_index()
snr = snr.dropna()

snr.columns = ["time", "sv", "snr"]

snr["sv_num"] = snr["sv"].str[1:].astype(int)

snr["constellation"] = 0

epoch_stats = snr.groupby("time")["snr"].agg(
    sat_count="count",
    mean_snr="mean",
    std_snr="std"
).reset_index()

snr = snr.merge(epoch_stats, on="time")

snr["label"] = 2

snr.to_csv("../output/foil_features.csv", index=False)

print("Saved foil_features.csv")
print("Rows:", len(snr))