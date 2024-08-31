import matplotlib.pyplot as plt

xArray = []
yArray = []

for x in range(-100,100):
    xArray.append(x)
    yArray.append(-x**2-5*x+6)

plt.plot(xArray, yArray)
plt.show()