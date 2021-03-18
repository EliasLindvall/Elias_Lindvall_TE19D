import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10)

y = 3*x+1




plt.plot(x,y, 'r', label='3x+1')
plt.legend(loc='upper left')

plt.show()