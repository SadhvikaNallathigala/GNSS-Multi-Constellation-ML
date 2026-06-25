import georinex as gr
import pandas as pd


def get_constellation(sv):
    if sv.startswith("G"):
        return "GPS"
    elif sv.startswith("R"):
        return "GLONASS"
    elif sv.startswith("E"):
        return "GALILEO"
    elif sv.startswith("C"):
        return "BEIDOU"
    elif sv.startswith("I"):
        return "NAVIC"
    elif sv.startswith("J"):
        return "QZSS"
    elif sv.startswith("S"):
        return "SBAS"
    return "OTHER"


def extract(obs_file, label):

    obs = gr.load(obs_file)

    snr_col = None

    for col in obs.data_vars:
        if col.startswith("S"):
            snr_col = col
            break

    print(f"Using SNR column: {snr_col}")

    df = obs[snr_col].to_dataframe().reset_index()

    df.columns = ["time", "sv", "snr"]

    df = df.dropna()

    df["constellation"] = df["sv"].str[0]

    df["sv_num"] = (
        df["sv"]
        .str.extract(r"(\d+)")
        .astype(int)
    )

    df["label"] = label

    return df


clear_df = extract(
    "../data/sadhvika_01.26o",
    0
)

metal_df = extract(
    "../data/metal_plate.26o",
    1
)

foil1_df = extract(
    "../data/sadhvika_foil.26o",
    2
)

foil2_df = extract(
    "../data/sadhvika_foil02.26o",
    2
)

final_df = pd.concat(
    [clear_df, metal_df, foil1_df, foil2_df],
    ignore_index=True
)

print(final_df.head())

print("\nClass Counts:")
print(final_df["label"].value_counts())

final_df.to_csv(
    "../output/gnss_dataset_v2.csv",
    index=False
)

print("\nDataset saved")