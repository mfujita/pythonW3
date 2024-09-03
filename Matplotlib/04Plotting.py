# Plotting
'''
A função plot() desenha os pontos (makers) do diagrama.
Por padrão, a função plot() desenha uma linha ponto a ponto.
A função receber os parâmetros para especificar os pontos no diagrama.
Parâmetro 1 → valores do eixo X
Parâmetro 2 → valores do eixo Y
Para ligar o ponto (1,3) até (8,10) é preciso passar 2 arrays: [1,8] e [3,10] para a função de desenhar o gráfico.
'''
# Exemplo: Desenhe uma linha de (1,3) até (8,10)
'''
import matplotlib.pyplot as plt
import numpy as np
X=np.array([1,8])
Y=np.array([3,10])
plt.plot(X,Y)
plt.show()
'''

# Plotting Without Line
# Para desenhar apenas os makers sem a linha que os liga, usa-se a notação 'o' que significa 'rings'.
'''
import matplotlib.pyplot as plt
import numpy as np
X=np.array([1,8])
Y=np.array([3,10])
plt.plot(X,Y,'o')
plt.show()
'''

# Multiple Points
# A condição de desenhar vários gráficos é que a quantidade de pontos do array com o pontos X e Y seja a mesma.
'''
import matplotlib.pyplot as plt
import numpy as np
X=np.array([1,2,6,8])
Y=np.array([3,8,1,10])
plt.plot(X,Y)
a1=np.array([1,8])
a2=np.array([3,10])
plt.plot(a1,a2)
plt.show()
'''

# Default X-Points → quando os valores do eixo X não forem especificados, os valores por padrão são 0,1,2,3,... até o tamanho do array com os valores do eixo Y.
import matplotlib.pyplot as plt
import numpy as np

Y = np.array([-10,5,-8,3,-8,7,0])
plt.plot(Y)
plt.show()