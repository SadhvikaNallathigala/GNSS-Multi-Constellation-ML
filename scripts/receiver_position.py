import georinex as gr

files = [
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\clear_sky.26o",
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\metal_plate.26o",
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\sadhvika_foil.26o",
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\SADHVIKA_SKY01.26o"
]

print("\nReceiver Positions\n")

for f in files:

    obs = gr.load(f, interval=60)

    pos = obs.attrs["position"]

    print(f.split("\\")[-1])

    print("X =", pos[0])
    print("Y =", pos[1])
    print("Z =", pos[2])

    print()