# constellation_stats.py

import gnss_lib_py as glp
import numpy as np

obs = glp.RinexObs("../data/SADHVIKA_SKY01.26o")

ids = obs["gnss_id"]

unique, counts = np.unique(ids, return_counts=True)

print("\nConstellation Statistics\n")

for u,c in zip(unique,counts):
    print(f"{u:10s} : {c}")