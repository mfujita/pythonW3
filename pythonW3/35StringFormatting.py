# String Formatting
# F-String foi introduzido na versão 3.6 e é a forma preferida de formatação

test = f'She is 25 years old.'
print(test)

# Placeholders and Modifiers
# Placeholders {} → variáveis, operadores, funções e modificadores para formatar o valor.

age = 26
print(f'She is {age} years old.')

# Modifiers → :
# .2f → 2 casas decimais
print(f'{10/3:.2f}')

# Perform Operations in F-Strings
# if...else
idade = 18
print(f'Você é {'maior' if idade>=18 else 'menor'} de idade.')

idade=10
print(f'Você é {'maior' if idade>=18 else 'menor'} de idade')

# Execute Functions in F-Strings
dever = 'mesmo se não estiver na escala'
print(f'Todos devem comparecer {dever.upper()}.')

speed = 100 # km/h
print(f'The speed was {speed/3.6:.2f} m/s')

# More Modifiers
# Separador de milhar
someNumber=12345
print(f'{someNumber:,}')

americanSystem = f'{someNumber:,}'
converted = americanSystem.replace(',','.')
print('converted: ', converted)

# Formatting Types
'''
:< alinhamento à esquerda
:> alinhamento à direita
:^ centraliza de acordo com o espaço disponível
:= distância entre o sinal de menos e o número.
:b converte para binário
:e notação científica usando e
:E notação científica usando E
:o converte para octal
:x converte para hexadecimal com minúsculas
:X converte para hexadecimal com maiúsculas
:% forma percentual
'''

print(f'Temperature is {-5:=6} degrees celsius') # Temperature is -    5 degrees celsius
print(f'10 = {10:b}')
print(f'10000000 = {10000000:e}')
print(f'10000000 = {10000000:E}')
print(f'10 = {10:o}')
print(f'15 = {15:x}')
print(f'15 = {15:X}')
print(f'1/4 = {1/4:%}')
print(f'1/4 = {1/4:.0%}')
print(f'2/3 = {2/3:.2%}')

# Index Numbers
fabricante = 'Toyota'
modelo = 'Corolla'
frase = 'A montadora {1} fabrica o {0}. O {1} é fabricado pela montadora {0}.'
print(frase.format(fabricante, modelo))

# Named Indexes
texto = 'O {linguagem} foi desenvolvoldo por {autor}.'
print(texto.format(linguagem='Python', autor='Guido van Rossum'))