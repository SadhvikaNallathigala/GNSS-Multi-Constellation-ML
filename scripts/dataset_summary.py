import georinex as gr
import numpy as np

files = {
    "METAL" : r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\metal_plate.26o",
    "FOIL"  : r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\sadhvika_foil.26o",
    "FOIL2" : r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\sadhvika_foil02.26o",
    "SKY01" : r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\SADHVIKA_SKY01.26o"
}

print("\nGNSS DATASET SUMMARY\n")

for name, file in files.items():

    obs = gr.load(file, interval=60)

    sats = len(obs.sv.values)
    epochs = len(obs.time.values)

    snr_cols = [c for c in obs.data_vars if c.startswith("S")]

    snr_values = []

    for col in snr_cols:
        vals = obs[col].values.flatten()
        vals = vals[~np.isnan(vals)]
        snr_values.extend(vals)

    mean_snr = np.mean(snr_values)

    print(f"{name}")
    print(f"Epochs     : {epochs}")
    print(f"Satellites : {sats}")
    print(f"Mean SNR   : {mean_snr:.2f}")
    print("-"*40)