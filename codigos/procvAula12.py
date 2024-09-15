import random
import xlsxwriter
from datetime import datetime

maximo = 5
dataVenda = []
listaNome1 = ['Tebaldo','Regis','Demostenes','Juca','Joelson','Miguelito','Matusalém','Felizberto','Anatonildo', 'Roberson']
listaNome2 = ['Vilcar','Fazana','Milor','Tabulante','Malaquias','Fintara','Giodize','Dalemar','Penfiani','Livalo']
nomesProntos = []
produtos = ['Fone com fio', 'Mouse 3 botões com fio','Fone bluetooth', 'Mousepad', 'Teclado 107 teclas', 'Adaptador de tomada', 'Filtro de linha', 'Cabo USB tipo C', 'Mouse wireless']
precos = [43.2, 22.8, 67.7, 15.1, 28.9, 5.7, 42.3, 19.5, 32.4]
comoPagar = ['Dinheiro','Pix','Cartão de débito','Cartão de crédito']

def criaDataVenda():
    dia = random.randint(1,30)
    mes = random.randint(6,7)
    return (str(dia)).zfill(2) +"/"+ (str(mes)).zfill(2) +"/2024"
    #return str(dia) +"/"+ str(mes)+"/2024"
    # return list((dia,mes,2024))

def produto_preco():
    sorteio = random.randint(0,len(produtos)-1)
    precoProduto = list((produtos[sorteio], precos[sorteio]))
    return precoProduto

def formaPagamento():
    sorteio = random.randint(0,len(comoPagar)-1)
    return comoPagar[sorteio]

def nomeVendedor():
    qtde = 0
    nomeSelecionado = []
    sobrenomeSelecionado = []

    while qtde < maximo:
        sorteio = random.randint(0, len(listaNome1)-1)
        nome = listaNome1[sorteio]
        sobrenome = listaNome2[sorteio]
        
        if nome not in nomeSelecionado:
            nomeSelecionado.append(nome)

        if sobrenome not in sobrenomeSelecionado:
            sobrenomeSelecionado.append(sobrenome)      
            qtde+=1

    for i in range(len(nomeSelecionado)):
        nomesProntos.append(nomeSelecionado[i] + " " + sobrenomeSelecionado[i])

nomeVendedor() # obtém os nomes de pessoas tantes vezes

def geraPlanilha():    
    qtde=0
    maximo = 100

    planilha = xlsxwriter.Workbook('Procv_aula12.xlsx')
    aba = planilha.add_worksheet()

    aba.write(f"A1","Data venda")
    aba.write(f"B1","Vendedor")
    aba.write(f"C1","Produto")
    aba.write(f"D1","Preço")
    aba.write(f"E1","Forma pagamento")

    while qtde < maximo:
        sorteado = random.randint(0,len(nomesProntos)-1)
        # time.sleep(0.1)
        produtoEpreco = produto_preco()
        #print(criaDataVenda(), f'{nomesProntos[sorteado]:<20}', f'{produtoEpreco[0]:<25}', f'{produtoEpreco[1]:>4}',f'{formaPagamento()}')
        formatacao = planilha.add_format({'num_format' : 'dd/mm/yyyy', 'align' : 'right'})
        data_da_venda = criaDataVenda()
        codigo = "%d/%m/%Y"
        dataFormatada = datetime.strptime(data_da_venda,codigo)
        aba.write_datetime(qtde+1, 0, dataFormatada, formatacao)
        #aba.write(f"A{qtde+2}",criaDataVenda())
        aba.write(f"B{qtde+2}",nomesProntos[sorteado])
        aba.write(f"C{qtde+2}",produtoEpreco[0])
        #aba.write(f"D{qtde+2}",produtoEpreco[1])
        aba.write_number(qtde+1,3,produtoEpreco[1])
        aba.write(f"E{qtde+2}",formaPagamento())

        aba.set_column('A:B',15)
        aba.set_column('B:C',20)
        aba.set_column('C:D',20)
        # aba.autofit('E')
        aba.set_column('E:F',20)
        qtde+=1
    planilha.close()

geraPlanilha()