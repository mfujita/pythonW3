# Binomial Distribution → é uma distribuição discreta.
# Descreve o resultado de resultados binários como "cara ou coroa".
# Os parãmetros:
# n: numero de tentativas
# p: probabilidade da ocorrência em cada tentativa
# size: o shape do array retornado (a quantidade de número de elementos em cada dimensão)
# Distribuição discreta → definida em conjutos separados de eventos. Por exemplo, "cara ou coroa" é um resultado discreto.

# Dado 10 tentaivas para cara ou coroa, gere 10 pontos
from numpy import random
print('random.binomial(n=10, p=0.5, size=10)')
array1= random.binomial(n=10, p=0.5, size=10)
print(array1) # [5 4 7 4 5 4 6 7 5 6]

# Visualization of Binomial Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# sns.displot(random.binomial(n=10, p=0.5, size=1000))
# plt.show()

# Difference Between Normal and Binomial Distribution
# A distribuição normal é contínua enquanto que a distribuição binomial é discreta, mas se houver pontos suficientes serão similares à distribuição normal com ajuste de loc e scale
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()