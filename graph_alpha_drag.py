
import matplotlib.pyplot as plt
import numpy

#x axis
x = [1, 2, 3, 4, 5, 10, 15]

#y axis
y = [1783, 3565, 5348, 7131, 8914, 17827, 26741]


plt.scatter(x, y)

plt.xlabel('angle')

plt.ylabel('drag')

plt.title('angle over drag')


plt.show()


fit = numpy.polyfit(x ,y, 1)

print(fit)