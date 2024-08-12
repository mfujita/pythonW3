# Zipf Distribution → Amostras baseadas na Lei de Zipf.
# Em um coleção, o n-ésimo termo é 1/n vezes o termo mais comum. Por exemplo, a 5ª palavra mais comum na língua inglesa é aproxidamente 1/5 da sua frequência com a palavra mais comum.
# 2 parâmatros:
# a → parâmetro da distribuição
# size → o shape do array retornado

# Gere uma amostra para a distribuição Zipf com parãmetro igual 2 com tamanho 2x3:
from numpy import random
array1=random.zipf(a=2, size=(2,3))
print('random.zipf(a=2, size=(2,3))')
print(array1)

# Visualization of Zipf Distribution
# faça uma amostra com 1000 pontos, mas plotando apenas aqueles com valores menores que 10 para um gráfico mais significativo

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

array2=random.zipf(a=2, size=1000)
sns.displot(array2[array2<10], kde=False)
plt.show()
