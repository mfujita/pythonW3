# Subplot
# A função subplot desenha múltiplos plots em uma figura.
'''
import matplotlib.pyplot as plt
import math as math
X1=[]
Y1=[]
Y2=[]
x=1
while x <=2000:
    X1.append(x)
    Y1.append(math.log(x))
    Y2.append(math.sqrt(x))
    x+=1
plt.subplot(1,2,1)
plt.plot(X1,Y1)
plt.subplot(1,2,2)
plt.plot(X1,Y2)
plt.show()
'''

# The subplot() Function → 3 parâmetros:
'''
Os 2 primeiros argumentos representam linhas e colunas.
No caso anterior tinha 1 linha e 2 colunas.
O 3º argumento é associado um índice ao plot. Então:
0 → função log()
1 → função sqrt() 
'''
# plt.subplot(1,2,1)
# plt.subplot(1,2,2)
# significa 1 linha, 2 colunas e cada plot ocupa uma posição.

# plt.subplot(2,1,1)
# plt.subplot(2,2,2)
# significa 2 linhas, 1 coluna e cada plot ocupa sua posição.
import matplotlib.pyplot as plt
import math as math
X1=[]
Y1=[]
Y2=[]
x=1
while x <=2000:
    X1.append(x)
    Y1.append(math.log(x))
    Y2.append(math.sqrt(x))
    x+=1
plt.subplot(2,1,1)
plt.plot(X1, Y1)
plt.title('log(x)')
plt.subplot(2,1,2)
plt.plot(X1,Y2)
plt.title('Raiz Quadrada(x)')
plt.suptitle('Funções matemáticas')
plt.show()

# Para o caso de desenhar 6 plots na disposição 2 linhas e 3 colunas:
'''
plt.subplot(2,3,1)
plt.subplot(2,3,2)
plt.subplot(2,3,3)
plt.subplot(2,3,4)
plt.subplot(2,3,5)
plt.subplot(2,3,6)
'''

# Title
# Cada plot tem seu título através da função plot()

# Super Title
# suptitle() adiciona um título para a figura inteira

