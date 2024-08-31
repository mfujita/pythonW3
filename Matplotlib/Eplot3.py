import matplotlib.pyplot as plt
import math as math

X1= []
Y1 = []

for x in range(0,361):
    X1.append(x)
    Y1.append(math.sin(10*x*math.pi/180))
plt.ylim((-5,5))
plt.plot(X1,Y1)
plt.show()