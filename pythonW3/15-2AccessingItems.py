# Accessing Items
# O acesso é feito através do nome da chave
celular = {
    "fabricante" : "samsung",
    "modelo" : "A34",
    "RAM" : "4 GB",
    "armazenamento" : "128 GB"
}
print(celular["modelo"])

# get() tem o mesmo efeito que o uso de colchetes e o nome da chave
print(celular.get("RAM"))

# keys() listam as chave do dictionary
print(celular.keys()) # dict_keys(['fabricante', 'modelo', 'RAM', 'armazenamento'])

celular["tela"] = "6,5 polegadas"
print(celular.keys()) # dict_keys(['fabricante', 'modelo', 'RAM', 'armazenamento', 'tela'])

# values()
print('values() → ', celular.values()) # dict_values(['samsung', 'A34', '4 GB', '128 GB', '6,5 polegadas'])

# Atualizando um valor:
celular["tela"] = "6,4 polegadas"
print('values() atulizado→ ', celular.values()) # dict_values(['samsung', 'A34', '4 GB', '128 GB', '6,4 polegadas'])

# items() → Retorna os itens do dictionary seja como lists ou tuples
print(celular.items()) # dict_items([('fabricante', 'samsung'), ('modelo', 'A34'), ('RAM', '4 GB'), ('armazenamento', '128 GB'), ('tela', '6,4 polegadas')]) 

# Check if Key Exists
if "armazenamento" in celular:
    print(celular["armazenamento"])


