# scripts/check_feature_files.py

import pandas as pd

files = {
    "ClearSky":"output/clear_sky_features.csv",
    "Metal":"output/metal_plate_features.csv",
    "Foil":"output/foil_features.csv"
}

for name,file in files.items():

    df = pd.read_csv(file)

    print("\n",name)
    print(df.head())
    print(df.columns)