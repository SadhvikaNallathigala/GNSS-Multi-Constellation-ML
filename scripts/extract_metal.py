import georinex as gr
import pandas as pd

obs = gr.load("../data/metal_plate.26o")

snr = obs["S1C"].to_dataframe().reset_index()
snr = snr.dropna()

snr.columns = ["time", "sv", "snr"]

snr.to_csv("../output/metal_plate_features.csv", index=False)

print(snr.head())
print("Saved metal plate features")