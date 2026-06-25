import georinex as gr

obs = gr.load("../data/metal_plate.26o")

print(obs.sv.values)