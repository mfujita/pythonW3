# Uniform Distribution → usada para descrever a probabilidade onde todo evento tem chances iguais de acontecer. Por exemplo, geraçãi de números aleatórios.
# São necessários 3 parãmetros:
# a → limite inferior. Por padrão 0.0
# b → limite superior. Por padrão 1.0
# size → o shape do array retornado.

# Crie uma amostra de distribuição normal 2x3
from numpy import random
array1=random.uniform(size=(2,3))
print('random.uniform(size=(2,3))')
print(array1)

# Visualization of Uniform Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.uniform(size=1000))
plt.show()