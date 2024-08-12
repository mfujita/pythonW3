# Pareto Distribution → é a distribuição 80/20 (20% dos fatores causam 80% dos resultados).
# Há 2 parâmetros
# a → parâmetro shape
# size → o o shape do array retornado

# Gere uma amostra da Distribuição de Pareto com shape igual 2 com tamanho 2x3
from numpy import random
array1=random.pareto(a=2, size=(2,3))
print('random.pareto(a=2, size=(2,3))')
print(array1)

# Visualization of Pareto Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()