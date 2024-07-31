# JSON
# Converter JSON para Python
import json
pessoa = '{"nome":"Zé", "cidade":"São Paulo", "diversao":"futebol", "comida":"feijoada"}'
convertido = json.loads(pessoa)
print(convertido["nome"])
# Observação: necessariamente o JSON deve ser envolvido por aspas simples enquanto que as chaves e valores por aspas duplas.

# Converter Python para JSON
carro = {
    "fabricante":"Toyota",
    "modelo":"Corolla",
    "potencia": "140cv",
    "motorizacao": 2.0
}
objJSON = json.dumps(carro)
print(objJSON)

# Esta lista de objetos pode converter para JSON:
# dict, list, tuple, string, int, float, True, False, None

# Converta de Python → JSON
print(json.dumps({'nome':'Edit','sobrenome':'Piaff'}), type(json.dumps({'nome':'Edit','sobrenome':'Piaff'})))
print(json.dumps(['arroz', 'feijão']))
print(json.dumps(('C#','Python','javascript')))
print(json.dumps("hello world"))
print(json.dumps(10))
print(json.dumps(3.15))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

todosTipos = {
    "nome":"teste",
    "idade":30,
    "casado":True,
    "divorciado":False,
    "filhos": ('Tica', 'Taca'),
    "cachorros": None,
    "carros" : [
        {"fabricante":"Honda", "modelo":"Civic"},
        {"fabricante":"Fiat", "modelo":"Toro"}
    ]
}

print(json.dumps(todosTipos))

# Formatar o resultado → facilidade na leitura dos dados definindo a quantidade de indentações
print(json.dumps(todosTipos, indent=4))

print(json.dumps(todosTipos, indent=4, separators=(". ", " = ")))

# Ordenar o resultado (sort_keys) → dispõe as chaves em ordem crescente
print('Valores com chaves em ordem crescente')
print(json.dumps(todosTipos, indent=4, sort_keys=True))