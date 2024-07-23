# Change Items
# Para trocar o valor, atribua um novo a sua chave
imovel = {
    "tipo" : "casa",
    "qtdeComodos" : 3,
    "qtdeBanheiros" : 1
}
imovel["qtdeBanheiros"] = 2
print(imovel) # {'tipo': 'casa', 'qtdeComodos': 3, 'qtdeBanheiros': 2}

# update() → o argumento deve ser um dictionary
imovel.update({"qtdeComodos" : 2})
print("update() → ", imovel) # update() →  {'tipo': 'casa', 'qtdeComodos': 2, 'qtdeBanheiros': 2}

