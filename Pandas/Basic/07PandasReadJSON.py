# Pandas Read JSON
import pandas as pd
df1=pd.read_json('C:\\github\\Pandas\\Basic\\data.json')
print(df1.to_string())

# Dictionary as JSON → objetos JSON tem o mesmo formato dos dicionários Python
relatorio= {
    "Nome" : {
        0: "Stenico Santana Garcia",
        1: "Ana Caroline Dutra De Melo",
        2: "Raquel Gusmão Pacheco",
        3: "Vinicius Martins Santana Santigo"
    },
    "Produto": {
        0: "Fone de ouvido",
        1: "Carregador de baterias",
        2: "Teclado 107 teclas",
        3: "Mouse sem fio"
    },
    "Valor" : {
        0: 53.5,
        1: 37.8,
        2: 45.2,
        3: 50.0
    },
    "Forma Pagamento" : {
        0: "Pix",
        1: "Cartão de Crédito",
        2: "Boleto",
        3: "Cartão de débito"
    }
}

df2=pd.DataFrame(relatorio)
print(df2)