import openpyxl

# diretorio = 'C:\\faculdades\\etec\\2024\\'
# disciplinas = ['analise de projeto de sistemas\\mencoes2bim.xlsx',
               # 'desenvolvimento de sistemas\\Mencoes2bimA.xlsx',
               # 'desenvolvimento de sistemas\\Mencoes2bimB.xlsx',
               # 'IP\\Mencoes2bim.xlsx',
               # 'programação de aplicativos mobile\\DSAMS3\\Mencoes2bim.xlsx',
               # 'programação de aplicativos mobile\\DSNT2C\\Mencoes2bim.xlsx',
               # 'programação de aplicativos mobile\\DSNT2D\\Mencoes2bim.xlsx',
               # 'programação de aplicativos mobile\\DSNT3B\\bimestre2bim.xlsx',
               # 'programacao web\\mencoes2bim.xlsx',
               # 'sistemas embarcados\\DSAMS2\\bimestre2bim.xlsx',
               # 'sistemas embarcados\\DSNT3B\\bimestre2bim.xlsx',
               # 'técnicas de programação e algoritmos\\bimestre2bimA.xlsx',
               # 'técnicas de programação e algoritmos\\bimestre2bimB.xlsx',
               # 'Tecnologia Da Informação Aplicada À Administração\\ANT3A\\mencoes2bim.xlsx',
               # 'Tecnologia Da Informação Aplicada À Administração\\ANT3B\\mencoes2bim.xlsx']
               
# disciplinas = ['programação de aplicativos mobile\\DSNT3B\\Mencoes.xlsx']


planilha = openpyxl.load_workbook('C:\\faculdades\\etec\\2024\\programação de aplicativos mobile\\DSNT3B\\Mencoes.xlsx')
aba = planilha['bimestre3']

for indice, linha in enumerate(aba.iter_rows(min_row=1)):
    nome = linha[0].value
    mencao1 = linha[1].value
    mencao2 = linha[2].value
    mencaoFinal = linha[3].value

    if mencao1 == 'MB' and mencao2 == 'MB' and mencaoFinal != 'MB':
        print(f'{nome:<42} {mencao1} {mencao2} {mencaoFinal}')