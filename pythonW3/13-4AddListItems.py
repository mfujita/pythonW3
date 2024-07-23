print("List Add List items")
fruits=["abacate","banana", "caqui"]
cars=["Toro","Civic","Corolla"]
print(fruits)
print(cars)
fruits.extend(cars)
print(fruits)
print(cars)
# Conclusão: List.extend() junta o conteúdo da 2º estrutura de dados (list, tuple, set, dict) com o primeiro e armazena no 1º List.

lista = [1,2,3]
tupla = ('a', 'b', 'c')
lista.extend(tupla)
print(lista)