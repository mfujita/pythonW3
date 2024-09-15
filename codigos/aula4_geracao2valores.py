import random
import xlsxwriter

repeticoes=20

def sortearNumeros():
    myList = []
    for num in range(repeticoes):
        myList.append(random.randint(0,9))
    return myList

planilha = xlsxwriter.Workbook("aula5exercicios.xlsx")


def criaVariasAbas(nomeAba):
    aba=planilha.add_worksheet(nomeAba)

    def escreveValorFlutuanteNaCelula(letra, listapi, listafrac):
        qtde=0
        formatoNumerico = planilha.add_format({'num_format' : '0.0'})
        for i in range(repeticoes):
            print(str(listapi[i])+","+str(listafrac[i]))
            valorNumerico=(float)(str(listapi[i])+"."+str(listafrac[i]))
            aba.write(f"{letra}{i+1}", valorNumerico, formatoNumerico)

    listapi = sortearNumeros()
    listafrac = sortearNumeros()
    escreveValorFlutuanteNaCelula('A', listapi, listafrac)
    listapi = sortearNumeros()
    listafrac = sortearNumeros()
    escreveValorFlutuanteNaCelula('B', listapi, listafrac)


criaVariasAbas("Folha1")
criaVariasAbas("Folha2")

planilha.close()