import os

files = [
    "../data/clear_sky.jps",
    "../data/metal_plate_02.jps"
]

for f in files:
    print(f)
    print("Exists:", os.path.exists(f))
    print("Size:", os.path.getsize(f), "bytes")
    print("-"*30)