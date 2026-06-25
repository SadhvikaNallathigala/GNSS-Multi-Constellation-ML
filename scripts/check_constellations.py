# check_constellations.py

import gnss_lib_py as glp
import numpy as np

obs = glp.RinexObs("../data/sadhvika_01.26o")

print("Unique GNSS IDs:")
print(np.unique(obs["gnss_id"]))