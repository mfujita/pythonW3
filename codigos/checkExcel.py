import openpyxl

diretorio = 'C:\\faculdades\\etec\\2024-1\\'
disciplinas = ['analise de projeto de sistemas\\mencoes2bim.xlsx',
               'desenvolvimento de sistemas\\Mencoes2bimA.xlsx',
               'desenvolvimento de sistemas\\Mencoes2bimB.xlsx',
               'IP\\Mencoes2bim.xlsx',
               'programação de aplicativos mobile\\DSAMS3\\Mencoes2bim.xlsx',
               'programação de aplicativos mobile\\DSNT2C\\Mencoes2bim.xlsx',
               'programação de aplicativos mobile\\DSNT2D\\Mencoes2bim.xlsx',
               'programação de aplicativos mobile\\DSNT3B\\bimestre2bim.xlsx',
               'programacao web\\mencoes2bim.xlsx',
               'sistemas embarcados\\DSAMS2\\bimestre2bim.xlsx',
               'sistemas embarcados\\DSNT3B\\bimestre2bim.xlsx',
               'técnicas de programação e algoritmos\\bimestre2bimA.xlsx',
               'técnicas de programação e algoritmos\\bimestre2bimB.xlsx',
               'Tecnologia Da Informação Aplicada À Administração\\ANT3A\\mencoes2bim.xlsx',
               'Tecnologia Da Informação Aplicada À Administração\\ANT3B\\mencoes2bim.xlsx']

for i in range(len(disciplinas)):
    planilha = openpyxl.open(diretorio + disciplinas[i])
    aba = planilha['ALUNOS']

    print(disciplinas[i])

    for indice, linha in enumerate(aba.iter_rows(min_row=1)):
        nome = linha[2].value
        mencao1 = linha[4].value
        mencao2 = linha[5].value
        mencaoFinal = linha[6].value

        if mencao1 == 'MB' and mencao2 == 'MB' and mencaoFinal != 'MB':
            print(f'{nome:<42} {mencao1} {mencao2} {mencaoFinal}')