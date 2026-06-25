# dataset_duration.py

import gnss_lib_py as glp

obs = glp.RinexObs("../data/SADHVIKA_SKY01.26o")

start = obs["gps_millis"][0]
end = obs["gps_millis"][-1]

hours = (end - start)/(1000*60*60)

print("Start GPS millis:", start)
print("End GPS millis  :", end)
print("Duration (hours):", hours)