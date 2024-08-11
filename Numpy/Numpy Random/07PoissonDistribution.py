# Poisson Distribution → é uma distribuição discreta.
# Estima quantas vezes um evento pode acontecer em um tempo específico. Por exemplo, se alguém come duas vezes por dia, qual é a probabilidade que coma uma terceira vez?
# Há 2 parãmetros:
'''
lam → taxa ou número conhecido de ocorrências.
size → O shape do array retornado
'''
from numpy import random
array1=random.poisson(lam=2, size=10)
print('random.poisson(lam=2, size=10)')
print(array1)

# Visualization of Poisson Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.poisson(lam=2, size=1000), kde=False)
plt.show()

# Difference Between Normal and Poisson Distribution
'''
Distribuição Normal → contínua
Distribuição de Poison → discreta
Podem ser similares se tiver certos valores de desvio padrão e média. 
'''

# Difference Between Binomial and Poisson Distribution
'''
Distribuição binomial tem 2 possíveis
Distribuição de Poisson tem uma qunatidade ilimitada de possibilidades
Mas para n muito grande e p próximo de zero, a distribuição binomial é quase idêntica à distribuição de Poisson, de modo que n * p é quase igual a lam.
'''