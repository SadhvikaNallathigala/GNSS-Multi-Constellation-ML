# position_difference.py

import numpy as np

sky = np.array([1218670.7823, 5961213.7517, 1908259.3463])

metal = np.array([1218672.1120, 5961213.5168, 1908263.0778])

foil = np.array([1218665.6462, 5961205.2314, 1908253.8763])

foil2 = np.array([1218674.9715, 5961213.3041, 1908255.4672])

print("Metal Plate Error (m):",
      np.linalg.norm(metal - sky))

print("Foil Error (m):",
      np.linalg.norm(foil - sky))

print("Foil02 Error (m):",
      np.linalg.norm(foil2 - sky))
