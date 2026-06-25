import georinex as gr
import pandas as pd

obs = gr.load("../data/sadhvika_01.26o")

features = []

for obs_type in ["S1C", "C1C", "L1C", "D1C"]:

    if obs_type in obs.data_vars:

        df = obs[obs_type].to_dataframe().reset_index()
        df = df.dropna()

        df.columns = ["time", "sv", obs_type]

        features.append(df)

merged = features[0]

for f in features[1:]:
    merged = pd.merge(
        merged,
        f,
        on=["time", "sv"],
        how="outer"
    )

merged.to_csv(
    "../output/raw_observations.csv",
    index=False
)

print(merged.head())
print("\nRows:", len(merged))