# Rayleigh Distribution → usada em processamento de sinal. Tem 2 parâmetros:
# scale → stddev. Decide quão achatdo a distribuição será. Padrão 1.0
# size → o shape do array retornado

# Gere uma amostra para a Distribuição de Rayleigh  com scale igual 2 com tamanho 2x3:
from numpy import random
array1=random.rayleigh(scale=2, size=(2,3))
print('random.rayleigh(scale=2, size=(2,3))')
print(array1)

# Visualization of Rayleigh Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.rayleigh(size=1000))
plt.show()

# Similarity Between Rayleigh and Chi Square Distribution
# uma unidade do stddev e grau de liberdade 2 da distribuição de Rayleigh e distribuição chi square representam as mesmas distribuições. 