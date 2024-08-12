# Chi Square Distribution → A distribuição qui-quadrado é usada como base para verificar a hipótese.
# 2 parâmetros:
# df → degreee of freedom
# size → o shape do array retornado

# Gere amostras para distribuição qui-quadrado com grau de liberdade igual 2 com tamanho 2x3:
from numpy import random
array1=random.chisquare(df=2, size=(2,3))
print('random.chisquare(df=2, size=(2,3))')
print(array1)

# Visualization of Chi Square Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(size=1000))
plt.show()