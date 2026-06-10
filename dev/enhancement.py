import numpy as np
import pylab as plt

x = np.linspace(-10, 10, num=101)
y = x**2
plt.plot(x, y)
plt.show()
# plt.savefig("parabola.png")
print(f"Plot saved to parabola.png ({x[0]:.0f} to {x[-1]:.0f})")
