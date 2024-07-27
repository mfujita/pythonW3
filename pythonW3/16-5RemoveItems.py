# Remove Items
# pop()
animal = {
    "tipo" : "cachorro",
    "raca" : "bulldog francês",
    "cores" : ['branco', 'marrom claro'],
    "patas" : 4
}
animal.pop("patas")
print(animal)

# popitem() → remove o último item
animal = {
    "tipo" : "cachorro",
    "raca" : "bulldog francês",
    "cores" : ['branco', 'marrom claro'],
    "patas" : 4
}
animal.popitem()
print('popitem() → ', animal) # popitem() →  {'tipo': 'cachorro', 'raca': 'bulldog francês', 'cores': ['branco', 'marrom claro']}

# del
del animal
# print(animal) # name 'animal' is not defined

# clear
animal = {
    "tipo" : "cachorro",
    "raca" : "bulldog francês",
    "cores" : ['branco', 'marrom claro'],
    "patas" : 4
}
animal.clear()
print('animal.clear() → ', animal) # animal.clear() →  {}
