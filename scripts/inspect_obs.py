# inspect_obs.py

import gnss_lib_py as glp

obs = glp.RinexObs("../data/sadhvika_01.26o")

print("Rows:", len(obs))
print("\nColumns:")
print(obs.rows)