import georinex as gr
import warnings

warnings.filterwarnings("ignore")

files = [
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\clear_sky.26o",
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\metal_plate.26o",
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\sadhvika_foil.26o",
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\sadhvika_foil02.26o",
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\SADHVIKA_SKY01.26o"
]

for file in files:

    print("\n" + "="*70)
    print("FILE :", file)
    print("="*70)

    try:

        obs = gr.load(
            file,
            interval=60
        )

        print("\nDataset Loaded Successfully")

        print("\nReceiver Position:")
        print(obs.attrs["position"])

        print("\nDataset Statistics")

        print("Epochs      :", len(obs.time))
        print("Satellites  :", len(obs.sv))

        print("\nSatellite List:")
        print(obs.sv.values)

        print("\nObservation Types:")
        print(list(obs.data_vars))

    except Exception as e:

        print("ERROR:", e)

print("\nFinished Parsing All Datasets")