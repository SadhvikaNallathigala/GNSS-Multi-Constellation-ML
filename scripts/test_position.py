import gnss_lib_py as glp

obs = glp.RinexObs("../data/sadhvika_01.26o")

print("OBS LOADED")

obs = glp.add_sv_states_rinex(obs)

print("SV STATES ADDED")

print(obs)