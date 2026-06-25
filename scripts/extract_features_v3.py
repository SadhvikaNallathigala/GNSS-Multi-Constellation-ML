import georinex as gr
import pandas as pd

def constellation_code(sv):
    if sv.startswith("G"):
        return 0
    elif sv.startswith("R"):
        return 1
    elif sv.startswith("E"):
        return 2
    elif sv.startswith("C"):
        return 3
    elif sv.startswith("I"):
        return 4
    else:
        return 9

def extract(obs_file, label, out_csv):

    print(f"Processing {obs_file}")

    obs = gr.load(obs_file)

    signal_column = None

    for candidate in ["S1C","S1X","S2I","S5X"]:
        if candidate in obs.data_vars:
            signal_column = candidate
            break

    if signal_column is None:
        print("No SNR field found")
        return

    print("Using:", signal_column)

    snr = obs[signal_column].to_dataframe().reset_index()
    snr = snr.dropna()

    snr.columns = ["time","sv","snr"]

    snr["sv_num"] = snr["sv"].str[1:].astype(int)

    snr["constellation"] = snr["sv"].apply(constellation_code)

    epoch_stats = snr.groupby("time")["snr"].agg(
        sat_count="count",
        mean_snr="mean",
        std_snr="std"
    ).reset_index()

    snr = snr.merge(epoch_stats,on="time")

    snr["label"] = label

    snr.to_csv(out_csv,index=False)

    print("Saved:",out_csv)
    print("Rows:",len(snr))


extract(
    "../data/sadhvika_01.26o",
    0,
    "../output/multi_clear_features.csv"
)

extract(
    "../data/sadhvika_foil.26o",
    1,
    "../output/foil1_features.csv"
)

extract(
    "../data/sadhvika_foil02.26o",
    1,
    "../output/foil2_features.csv"
)