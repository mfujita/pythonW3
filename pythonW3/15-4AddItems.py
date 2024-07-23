# Add Items
carro = {
    "fabricante" : "Toyota",
    "modelo" : "Cross",
    "cambio" : "automático"
}
carro["cor"] = "preto"
print(carro) # {'fabricante': 'Toyota', 'modelo': 'Cross', 'cambio': 'automático', 'cor': 'preto'}

# update()
carro.update({"ano" : 2024})
print(carro) # {'fabricante': 'Toyota', 'modelo': 'Cross', 'cambio': 'automático', 'cor': 'preto', 'ano': 2024}

