import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import polynomial as P
#x axis
x = [0.1839, 0.1821, 0.1818, 0.1805, 0.3669, 0.3611, 0.3686, 0.3720]

#y axis
y = [8269800, 12404700, 16539600, 20674500, 11011428, 16517142, 22022857, 27528571]

plt.scatter(x, y)

#polynomial = p.fit(x, y, 1)

#fx, fy = p.linspace(100)

plt.xlabel('angle')

plt.ylabel('Lift')

plt.title('angle over lift')

plt.show()