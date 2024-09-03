# Grid 
# A função grid() adicional linhas de grade ao plot.
import matplotlib.pyplot as plt
import math as math
X=[]
Y=[]
x=1
while x <= 7200:
    X.append(x)
    Y.append(math.sin(x*math.pi/180)/x)
    x+=1
plt.title('Amortecimento')
plt.xlabel('Graus')
plt.ylabel('sin(10x)/x')
plt.grid(axis='y', color='blue', linestyle='-', linewidth='1')
plt.plot(X,Y)
plt.show()

# Specify Which Grid Lines to Display
# O parâmetro axis da função grid() especifica quais linhas devem ser mostradas.
# Os valores são x, y e both. Padrão é both.

# Set Line Properties for the Grid
# As linhas de grade podem ser configuradas com as opções:
# grid(color='color', linestyle='linestyle', linewidth='linewidth')