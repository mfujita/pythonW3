# Optimizers
# Optimizers in SciPy
# Optimizers são conjuntos de procedimentos definidos em SciPy que tanto encontra o valor mínimo da função ou a raiz da equação.

# Optimizing Functions
# Essencialmente, todos os algoritmos em Machine Learning não são nada mais do do que uma equação complexa que precisa ser minimizada com a ajuda de uma informação dada.

# Roots of an Equation
# NumPy é capaz de achar as raizes de equações polinomiais e lineares, mas não as raizes de uma equação não linear como x + cos(x)
# Por esta razão use-se a função optimiza.root() do SciPy.
# Esta função precisa de 2 argumentos:
# 1. fun → uma função que representa uma equação
# 2. xo → um valor inicial estimado para a raiz.
# A função retorna um objeto com a informação sem considerar a solução.
# A solução real é dada atribuindo x de um objeto retornado.

# Exemplo: encontre a raiz da equação x + cos(x)

from scipy.optimize import root
from math import cos
def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)
print(myroot.x)
'''
return x + cos(x)
[-0.73908513]    # radians
'''

# O objeto retornado contém mais informações.
print(myroot)
'''
 message: The solution converged.
 success: True
  status: 1
     fun: [ 0.000e+00]
       x: [-7.391e-01]
  method: hybr
    nfev: 11
    fjac: [[-1.000e+00]]
       r: [-1.674e+00]
     qtf: [-2.668e-13]
'''

# Minimizing a Function
# Uma função é representada por uma curva que pontos altos e pontos baixos.
# Pontos altos são chamados de máxima.
# Pontos baixos são chamados mínima.
# O ponto mais alto de toda curva é chamado de máximo global uma vez que o restante da curva é chamada de máxima local.
# O ponto mais baixo de toda curva é chamado de globla mínimo uma vez que o restabte da curva é chamado de mínimo local.

# Finding Minima
'''
Nós podemos usar a função scipy.optimize.minimize() para minimizar a função.
A função minimize() precisa dos seguintes argumentos:
1. fun → a função que representa a função
2. xo → um valor inicial estimado para a raiz.
3. method → o nome do método a ser usado:
'CG'
'BFGS'
'Newton-CG'
'L-BFGS-B'
'TNC'
'COBYLA'
'SLSQP'
4. callback → a função chamada depois de cada iteração de optimização.
5. option → um dicionário com as definições extras:
{
    "disp": boolean - print detailed description
    "gtol": number - the tolerance of the error
}
'''

# Exemplo: minimize a função x² + x + 2 com BFGS
from scipy.optimize import minimize
def eqn(x):
    return x**2 + x + 2
mymin=minimize(eqn,0, method='BFGS')
print('minimize(eqn,0, method=\'BFGS\')')
print(mymin)
'''
message: Optimization terminated successfully.
  success: True
   status: 0
      fun: 1.75
        x: [-5.000e-01]
      nit: 2
      jac: [ 0.000e+00]
 hess_inv: [[ 5.000e-01]]
     nfev: 8
     njev: 4
'''