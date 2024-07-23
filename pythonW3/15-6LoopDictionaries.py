# Loop Dictionaries
monitor = {
    "fabricante" : "aoc",
    "tamanho" : "21,5 polegadas",
    "resolução" : "full HD"
}

# imprime as chaves
print("toda sas chaves")
for item in monitor:
    print(item + ' ', end=' ') # fabricante  tamanho  resolução
print()

# imprime todos os valores
print('# imprime todos valores')
for item in monitor:
    print(monitor[item], end=' ') # aoc 21,5 polegadas full HD
print()

# imprime todos os valores
print ("imprime todos os valores")
for item in monitor.values():
    print(item, end=' ')
print()

#imprime todas as chaves
print("imprime todas as chaves")
for chave in monitor.keys():
    print(chave)
print()

# imprimir todas as chaves e valores
for i,j in monitor.items():
    print(f'{i:<12} {j:<10}')


