import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")

a = np.array([0, 10, 100])
b = a * 2
plt.figure(10)
plt.plot(a, b)
plt.show()