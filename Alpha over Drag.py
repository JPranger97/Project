
import matplotlib.pyplot as plt
import numpy

#x axis
x = [1, 2, 3, 4, 5, 10, 15]

#y axis
y = [455, 484, 532, 600, 686, 1409, 2612]


plt.scatter(x, y)

plt.xlabel('angle')

plt.ylabel('drag')

plt.title('angle over drag')


plt.show()


fit = numpy.polyfit(x ,numpy.log(y), 1)

print(fit)




