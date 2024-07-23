# Copy Dictionary
comida = {
    "tipo" : "churrasco",
    "local" : "sítio",
    "acompanha" : "cerveja"
}
festa = comida.copy()
print(festa)

# dict()
comemoracao = dict(comida)
print(comemoracao, 'type(comemoracao) → ', type(comemoracao))
