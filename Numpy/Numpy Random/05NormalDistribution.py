# Normal Distribution → Também chamada de Distribuição de Gauss
'''
Ajusta a distribuiçao de probabilidades de muitos eventos como Pontuação de QI, batimento cardíaco etc.
Para obter a Distribuição Normal → random.normal() com 3 parãmetros:
loc (mean): o pico do sino
scale (desvio padrão): especifica o quão plana deve ser a distribuição do gráfico.
size: o shape do array retornado
'''
# Gere uma distribuição normal aleatória de dimensão 2x3:
from numpy import random
print('normal')
array1=random.normal(size=(2,3))
print(array1)

# Gere uma distribuição normal de dimensão 2x3 que a média = 1 e o desvio padrão = 2
print('média = 1 e o desvio padrão = 2')
array2=random.normal(loc=1, scale=2, size=(2,3))
print(array2)

# Visualization of Normal Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sns.displot(random.normal(size=1000), hist=False)
sns.displot(random.normal(size=500))
plt.show()