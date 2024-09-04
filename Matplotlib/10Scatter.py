# Scatter → função scatter()
# Plota um ponto por observação. É preciso um array para os pontos do eixo X e outro array para os pontos do eixo Y.
'''
import matplotlib.pyplot as plt
X = [7,   2, 10, -13, 8,  -4, 0, -19, 14, -18, 4]
Y = [56, 14,  7,  11, 25, 19, 10, 39, 24,  18, 31]
plt.scatter(X,Y)
plt.show()
'''

# Compare Plots
'''
import matplotlib.pyplot as plt
X = [5,7,8,7,2,17,2,9,4,11,12,9,6]
Y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(X,Y, color = 'hotpink')

X = [2,2,8,1,15,8,12,9,7,3,11,4,7,14,12]
Y = [100,105,84,105,90,99,90,95,94,100,79,112,91,80,85]
plt.scatter(X,Y, color = '#12359A')
plt.show()
'''

# Colors
# Na função scatter() usa-se o parâmetro color

# Color Each Dot
# Para especificar cada cor do marker, usa-se o argumento c.
# Observação: Não pode usar o argumento color.
'''
import matplotlib.pyplot as plt
X=[5,7,8,7,2,17,2,9,4,11,12,9,6]
Y=[99,86,87,88,111,86,103,87,94,78,77,85,86]
colors=["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"]
plt.scatter(X,Y, c=colors)
plt.show()
'''

# ColorMap
# Um colormap é como uma lista de cores sendo que cada cor tem um valor no intervalo de 0 a 100.

# How to Use the ColorMap
# Na função scatter() use o argumento cmap com valor do colormap. Por exemplo, 'viridis' que é um colormap.
# Em seguida crie um array com valores de 0 a 100 sendo um valor para cada ponto do plot scatter.
'''
import matplotlib.pyplot as plt
X=[5,7,8,7,2,17,2,9,4,11,12,9,6]
Y=[99,86,87,88,111,86,103,87,94,78,77,85,86]
colors=[0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100]
plt.scatter(X, Y, c=colors, cmap='rainbow')
plt.colorbar()
plt.show()
'''

# Size → muda o tamanho dos pontos com o argumento s.
# Certifique-se quantidade de elementos do array SIZE é igual aos dos array com os pontos X e Y.
'''
import matplotlib.pyplot as plt
X=[5,7,8,7,2,17,2,9,4,11,12,9,6]
Y=[99,86,87,88,111,86,103,87,94,78,77,85,86]
sizes=[20,50,100,200,500,1000,60,90,10,300,600,800,75]
plt.scatter(X, Y, s=sizes, alpha=0.5)
plt.show()
'''

# Alpha → os pontos tornam-se transparentes com o argumento alpha

# Combine Color Size and Alpha
import matplotlib.pyplot as plt
import numpy as np
X=np.random.randint(100, size=100)
Y=np.random.randint(100, size=100)
colors=np.random.randint(100, size=100)
sizes=10 * np.random.randint(100, size=100)
plt.scatter(X, Y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()
