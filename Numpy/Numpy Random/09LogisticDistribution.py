# Logistic Distribution → usada para descrever um crescimento
# Usado extensivamente em machine learning em regressão logistica, redes neurais etc
# # Há 3 parâmetros:
# loc - média que localiza o pico. Padrão é 0.
# scale - desvio padrão, o quão plano é a distribuição. Padrão é 1.
# size - o shape do array retornado.

# Desenhe uma amostra 2x3 de uma distribuição logística com média igual a 1 e devstd igual a 2.0
from numpy import random
array1=random.logistic(loc=1, scale=2, size=(2,3))
print('random.logistic(loc=1, scale=2, size=(2,3))')
print(array1)

# Visualization of Logistic Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.logistic(size=(1000)))
plt.show()

# Difference Between Logistic and Normal Distribution
# Distribuição logística tem mais área sob as caudas significando mais possibilidade de ocorrência de um evento mais distante da média.
# Para valores maiores de escala (devstd) as distribuições normal e logística são quase idênticas exceto pelo pico.

sns.displot(random.normal(scale=2, size=1000), label='Normal')
sns.displot(random.logistic(size=1000), label='Logistic')
plt.show()