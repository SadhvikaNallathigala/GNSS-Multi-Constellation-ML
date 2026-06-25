# check_files.py

import os

folder = r"C:\Users\USER\OneDrive\Desktop\GNSS_ML_Project\data"

print("Files found:\n")

for f in os.listdir(folder):
    if f.endswith(".26o"):
        print(f)