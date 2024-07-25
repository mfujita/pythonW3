# If Else
# Short Hand If → if em uma linha
a = 33
b = 12
if a >b : print("a é maior que b")

# Short Hand If ... Else → if else em uma linha
print("b é maior que a") if b > a else print("a é MAIOR que b")

# Operador ternário com 3 condições
a = 2
b = 2
print("a é maior que b") if a > b else print("a é igual a b") if a == b else print(" b maior que a")

a = 1
b = 2
c = 3
if a < b and b < c:
    print("Ambas comprações são verdadeiras.")

if a > b or b < c:
    print("Uma das condições resultou verdadeiro.")

if not a > b:
    print("Se esta mensagem foi impressa é porque o NOT tornou-a verdadeira.")

# Nested If
valor = 10
if valor > 5:
    print('Maior que 5')
    if valor > 20:
        print('Maior que 20')
    else:
        print('Menor que 20.')

# The pass Statement → Para evitar erro quando não há instruções para a condição verdadeira do IF.
v1 = 1
v2 = 2
if v2 > v1:
    pass
