# Exponential Distribution → é usada para descrever o tempo até o próximo evento. Por exemplo: falha/sucesso.
# Há 2 parâmetros:
# scale → inverso da taxa (veja lam em distribuição de Poisson). Padrão é 1.0
# size → o shape do array retornado
# lam da distribuição de Poisson → a taxa ou número de ocorrência.

# Gere uma amostra para uma distribuição exponencial com scale igual 2.0 com dimensão 2x3
from numpy import random
array1=random.exponential(scale=2, size=(2,3))
print('random.exponential(scale=2, size=(2,3))')
print(array1)

# Visualization of Exponential Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.exponential(size=100))
plt.show()

# Relation Between Poisson and Exponential Distribution
'''
Distribuição de Poisson lida com número de ocorrências de um evento em um período de tempo.
Distribuição exponencial lida com o tempo entre estes eventos.
'''