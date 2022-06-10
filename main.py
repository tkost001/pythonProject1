import numpy as np
import matplotlib.pyplot as plt
import math
x = np.linspace(0, 2*math.pi, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y)
plt.show()