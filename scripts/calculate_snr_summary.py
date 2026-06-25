import pandas as pd

clear = pd.read_csv("output/clear_sky_features.csv")
metal = pd.read_csv("output/metal_plate_features.csv")
foil = pd.read_csv("output/foil_features.csv")

print("\nMean SNR Values")
print("-" * 30)

print("Open Sky    :", round(clear["snr"].mean(), 2))
print("Metal Plate :", round(metal["snr"].mean(), 2))
print("Silver Foil :", round(foil["snr"].mean(), 2))