import georinex as gr

obs = gr.load(
    r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data\SADHVIKA_SKY01.26o",
    interval=60
)

print(obs)