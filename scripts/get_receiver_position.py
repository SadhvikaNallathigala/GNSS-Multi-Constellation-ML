# get_receiver_position.py

import georinex as gr

obs = gr.load("../data/SADHVIKA_SKY01.26o")

print(obs.attrs["position"])