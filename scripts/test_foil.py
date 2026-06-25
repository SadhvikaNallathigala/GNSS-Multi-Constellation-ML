import georinex as gr

obs = gr.load("../data/sadhvika_foil.26o")

print(obs)

print("\nVariables:")
print(list(obs.data_vars))