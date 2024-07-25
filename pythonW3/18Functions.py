# Functions

def imprimeNome(nome):
    print("Hello, " + nome + "!")

imprimeNome('Pasqualina')
imprimeNome('Tiburcio')
imprimeNome('Jeguenildo')

# Parâmetros são os valores que estão entre parênteses de uma função
# Argumentos são enviados para função quando são chamadas.

# Arbitrary Arguments, *args 
# Quando o número de argumentos é diferente dos parâmetros, use * antes da parâmetro
def imprimeCarros(*carro):
    print('Disponível um ' + carro[1])

imprimeCarros('Gol','Uno','Fox','BMW')

# Keyword Arguments → A ordem dos parâmetros/argumentos independente do uso de keys
# várias funções e várias chamadas resultam em apenas a última função ser executada o mesmo número de chamadas.
def imprime_almoco(t3, t2, t1):
    print('Sera servido ' + t1)

def imprime_almoco(t3,t2,t1):
    print('O cardápio é ' + t2)

def imprime_almoco(t3,t2,t1):
    print('Hoje tem ' + t3)

imprime_almoco(t1='churrasco', t2='feijoada', t3='variedade de massas')
imprime_almoco(t1='churrasco', t2='feijoada', t3='variedade de massas')
imprime_almoco(t1='churrasco', t2='feijoada', t3='variedade de massas')

# Arbitrary Keyword Arguments, **kwargs
# Quando não se sabe a quantidade de argumentos de um dicionário
def imprime_SO(**so):
    print('O projeto usará ' + so['lin'])

imprime_SO(win='windows', lin='linux')

def print_greetings(nome, **pronome):
    print('Ele se apresentou como ' + pronome['sr'] + " " + nome)

print_greetings('Felizbeto', dr='dr.', sr='sr.')

# Default Parameter Value
def print_job(job='programador'):
    print('Trabalho como ' + job)

print_job('engenheiro')
print_job('professor')
print_job()
print_job('médico')

# Passing a List as an Argument → enviando uma lista, recebe uma lista
def refeicoes(comida):
    for item in comida:
        print(item)

refeicoes(['churrasco', 'salada', 'vinagrete', 'pão'])

# Return Values
def tabuada(numero):
    return 5 * numero

print(tabuada(7))
print(tabuada(3))
print(tabuada(0))

# The pass Statement → para evitar erro ao chamar uma função vazia, usa-se pass
def evita_erro():
    pass

evita_erro()

# Positional-Only Arguments → são especificadas por , /
def funcao(numero, /): 
    print(numero) 

funcao(3) # Se fizesse numero = 3 quando usa-se positional-only causaria ERRO

# Substitui quando é necessário atribuir um valor para o argumento. O nome dado ao argumento deve ser o mesmo que do parãmetro
def justifica_positional_only(numero):
    print(numero)

justifica_positional_only(numero=8)

# Keyword-Only Arguments
# Para especificar que a função tem somente Keyword-Only Arguments, adicione *, antes dos argumentos
def print_number(*, x):
    print(x)

print_number(x= 10)

# Combine Positional-Only and Keyword-Only
# Antes do / são positional-only e depois do * são keyword-only
def expressao_matematica(a,b,/,*,c,d,):
    print(a+b+c+d)

expressao_matematica(1,5,c=4,d=6)

# Recursão
print('Recursão')
def tri_recursao(numero):
    if numero > 0:
        resultado = numero + tri_recursao(numero - 1)
        print(resultado)
    else:
        resultado=0
    return resultado

tri_recursao(5)