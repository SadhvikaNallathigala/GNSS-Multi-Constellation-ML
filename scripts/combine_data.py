import pandas as pd

clear = pd.read_csv("../output/clear_sky_features.csv")
metal = pd.read_csv("../output/metal_plate_features.csv")
foil = pd.read_csv("../output/foil_features.csv")

dataset = pd.concat(
    [clear, metal, foil],
    ignore_index=True
)

dataset.to_csv(
    "../output/gnss_dataset_v2.csv",
    index=False
)

print(dataset.head())

print("\nClass Counts:")
print(dataset["label"].value_counts())

print("\nDataset saved")