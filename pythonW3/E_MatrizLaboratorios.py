import numpy as np

geral = np.array([
    ["Lab1-DAIVES-Algoritmos-CC", "Lab1-YURI-Multimida-SI", "Lab1-YURI-Imagens-CC", "Lab1-VALMIR-Design", "Lab1-MARCOS ANTÔNIO-EngQui-Proje"],
    ["Lab1-DAIVES-Algoritmos-CC", "Lab1-YURI-Logica-SI", "Lab1-YURI-Imagens-CC", "Lab1-Jose Ribeiro-Contabeis", ""],
    ["Lab2-SINCLAIR-Design", "Lab2-DANIEL-Arquitetura-CC", "Lab2-SAMARA-Simulação-Eng", "Lab2-DANIEL-Estrutura-CC", "Lab2-LAURA MARIA-TCC-EngPr"],
    ["", "Lab2-DANIEL-Arquitetura-CC", "", "Lab2-DANIEL-Estrutura-CC", "Lab2-LAURA MARIA-TCC-EngPr"],
    ["Lab3-DANIEL-Arquitetura-CC", "Lab3-FABIO-Estatística-EngCV", "Lab3-FABIO-Estatística-EngPr", "Lab3-FABIO-Algebra-EngMc", "Lab3-Mariana Costa-EngOv"],
    ["Lab3-DANIEL-Arquitetura-CC", "Lab3-FABIO-Estatistica-EngCV", "Lab3-FABIO-Estatística-EngPr", "Lab3-FABIO-Estatística-EngMc", "Lab3-Mariana Costa-EngOv"],
    ["Lab4-ROSEMARY-Projeto Digital-Engev", "Lab4-SEBASTIÃO-Sistemas-CC", "Lab4-LUCAS SERAFIM-Sistemas-CC", "Lab4-ROSEMARY-Projeto Digital-Engel", "Lab4-LUCAS SERAFIM-Sistemas-CC"],
    ["Lab4-Mariana Costa-Engov-Topicos", "Lab4-SEBASTIÃO-Sistemas-CC", "Lab4-LUCAS SERAFIM-Sistemas-CC", "Lab4-ROSEMARY-Projeto Digital-Engmec", "Lab4-LUCAS SERAFIM-Sistemas-CC"],
    ["Lab5-VALMIR-Design", "Lab5-SINCLAIR-Design", "Lab5-VALMIR-Design", "Lab5-SINCLAIR-Design", "Lab5-Laisa Lemes-Design"],
    ["Lab5-SINCLAIR-Design", "Lab5-SINCLAIR-Design", "Lab5-VALMIR-Design", "Lab5-SINCLAIR-Design", "Lab5-Laisa Lemes-Design"],
    ["Lab6-SEBASTIÃO-Sistemas-CC", "Lab6-VALMIR-Design", "Lab6-SANTACLARA-Algoritmos-CC", "Lab6-Paulo César-Estr Dados-SI", "Lab6-SEBASTIÃO-Sistemas-CC"],
    ["Lab6-SEBASTIÃO-Sistemas-CC", "Lab6-VALMIR-Design", "Lab6-SANTACLARA-Algoritmos-CC", "Lab6-Paulo César-Estr Dados-SI", "Lab6-SEBASTIÃO-Sistemas-CC"],
    ["Lab7-BRUNO HENRIQUE-CC", "Lab7-Marcos Antônio-EngPr", "Lab7-FUJITA-Estrutura de Dados-CC", "Lab7-SANTACLARA-Banco-SI", ""],
    ["Lab7-BRUNO HENRIQUE-CC", "Lab7-Marcos Antônio-EngPr", "Lab7-FUJITA-Estrutura de Dados-CC", "Lab7-SANTACLARA-Banco-SI", ""],
    ["Lab8-RAUL CESAR-Algoritmos-CC", "Lab8-FUJITA-Interface-CC", "Lab8-RAUL CESAR-Logica-CC", "Lab8-FUJITA-Arquitetura-SI", "Lab8-SANTACLARA-Banco-SI"],
    ["Lab8-RAUL CESAR-Algoritmos-CC", "Lab8-RAUL CESAR-Logica-CC", "Lab8-TAGLIETTA-SO-CC", "Lab8-TAGLIETTA-SO-CC", "Lab8-SANTACLARA-Banco-SI"]
])

def imprimeHorariosLaboratorios():
    for i in range(len(geral)):
        print(f'{geral[i][0]:<30} {geral[i][1]:<30} {geral[i][2]:<30} {geral[i][3]:<30} {geral[i][4]:<30}')

def exibeHorarioProfessor():
    horProf = [[]]
    j=0
    dia=0
    periodo=0
    nome='FUJITA' # input('Nome do professor: ')
    for linha in geral:
        for coluna in linha: 
            print(coluna, end=' ')
        print()
        #     if geral[linha][coluna] == nome:
        #         horProf[dia][periodo] = geral[linha][coluna]

exibeHorarioProfessor()