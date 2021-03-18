# Uppgift 4)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2)

y = x**2-1

plt.plot(x,y, 'r', label='x^2')
plt.legend(loc='upper left')

plt.show()