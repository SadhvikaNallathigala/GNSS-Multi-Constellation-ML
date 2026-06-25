import georinex as gr
import pandas as pd

def constellation_code(sv):
    if sv.startswith("G"):
        return 0   # GPS
    elif sv.startswith("R"):
        return 1   # GLONASS
    elif sv.startswith("E"):
        return 2   # Galileo
    elif sv.startswith("C"):
        return 3   # BeiDou
    elif sv.startswith("I"):
        return 4   # NavIC
    else:
        return 9

def extract(obs_file, label, out_csv):
    obs = gr.load(obs_file)

    snr = obs["S1C"].to_dataframe().reset_index()
    snr = snr.dropna()

    snr.columns = ["time", "sv", "snr"]

    snr["sv_num"] = snr["sv"].str[1:].astype(int)
    snr["constellation"] = snr["sv"].apply(constellation_code)

    epoch_stats = snr.groupby("time")["snr"].agg(
        sat_count="count",
        mean_snr="mean",
        std_snr="std"
    ).reset_index()

    snr = snr.merge(epoch_stats, on="time")

    snr["label"] = label

    snr = snr[[
        "time",
        "sv",
        "snr",
        "sv_num",
        "constellation",
        "sat_count",
        "mean_snr",
        "std_snr",
        "label"
    ]]

    print(snr.head())

    snr.to_csv(out_csv, index=False)

extract("../data/clear_sky.26o", 0, "../output/clear_sky_features.csv")
extract("../data/metal_plate.26o", 1, "../output/metal_plate_features.csv")