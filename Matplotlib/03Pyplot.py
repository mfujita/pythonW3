# Pyplot
# Desenhe uma linha da posição (0,0) até (6,250)
import matplotlib.pyplot as plt
import numpy as np

arrayX=np.array([0,6])
arrayY=np.array([0,250])
plt.plot(arrayX, arrayY)
plt.show()