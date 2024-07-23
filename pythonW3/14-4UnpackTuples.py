# Unpack Tuples
# Packing
tupla1 = ("um", "dois", "tres")

# Unpacking a tuple:
(v1, v2, v3) = tupla1
print(f"v1={v1}  v2={v2} v3={v3}")

# Using Asterisk
# Quando o número de variáveis coincide com o de valores, cada variável recebe seu respectivo valor.
# Quando há diferença entre o número de variáveis e o de valores, a variável com * recebe todos os valores até que as demais variáveis tenham apenas um valor.
tupla2=("um", "dois", "tres","quatro", "cinco")
print("*n3")
(n1, n2, *n3) = tupla2
print(n1)
print(n2)
print(n3)

print("*n2")
(a1, *a2, a3) = tupla2
print(a1)
print(a2)
print(a3)