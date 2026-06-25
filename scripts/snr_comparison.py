import pandas as pd
import matplotlib.pyplot as plt

means = {
    "Open Sky":43.31,
    "Metal":33.89,
    "Foil":31.55
}

plt.figure(figsize=(8,5))

plt.bar(
    means.keys(),
    means.values()
)

plt.ylabel("Mean SNR (dB)")
plt.title("Mean SNR Comparison")

plt.savefig(
    "output/mean_snr_comparison.png",
    dpi=300
)

plt.show()