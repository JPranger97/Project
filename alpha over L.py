import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial import polynomial as P
#x axis
x = [1, 2, 3, 4, 5, 10, 15]

#y axis
y = [1783, 3565, 5348, 7131, 8914, 17827, 26741]

plt.scatter(x, y)

polynomial = p.fit(x, y, 1)

fx, fy = p.linspace(100)

plt.xlabel('angle')

plt.ylabel('Lift')

plt.title('angle over lift')

plt.plot(fx, fy)

#plt.show()

#fit = numpy.polyfit(x ,numpy.log(y), 1)

#print(fit)