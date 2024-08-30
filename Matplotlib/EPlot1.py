# Desenhe o gráfico em 2 segmentos:
# 1. Do ponto (0,0) até (10,10)
# 2. Do ponto (10,10) até (20,0)
import matplotlib.pyplot as plt
import numpy as np
x1=np.array([0,10])
y1=np.array([0,10])
x2=np.array([10,20])
y2=np.array([10,0])

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()