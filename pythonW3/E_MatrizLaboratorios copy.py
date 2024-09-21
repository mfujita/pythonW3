geral = [
    ["Lab1-DAIVES-Algoritmos-CC", "Lab1-YURI-Multimida-SI", "Lab1-YURI-Imagens-CC", "Lab1-VALMIR-Design-", "Lab1-MARCOS ANTÔNIO-EngQui-Proje"],
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
    ["Lab7-BRUNO HENRIQUE-semMateria-CC", "Lab7-Marcos Antônio-EngPr", "Lab7-FUJITA-Estrutura de Dados-CC", "Lab7-SANTACLARA-Banco-SI", ""],
    ["Lab7-BRUNO HENRIQUE-semMateria-CC", "Lab7-Marcos Antônio-EngPr", "Lab7-FUJITA-Estrutura de Dados-CC", "Lab7-SANTACLARA-Banco-SI", ""],
    ["Lab8-RAUL CESAR-Algoritmos-CC", "Lab8-FUJITA-Interface-CC", "Lab8-RAUL CESAR-Logica-CC", "Lab8-FUJITA-Arquitetura-SI", "Lab8-SANTACLARA-Banco-SI"],
    ["Lab8-RAUL CESAR-Algoritmos-CC", "Lab8-RAUL CESAR-Logica-CC", "Lab8-TAGLIETTA-SO-CC", "Lab8-TAGLIETTA-SO-CC", "Lab8-SANTACLARA-Banco-SI"]
]
horProf = [['','','','',''],['','','','','']]
nome="FUJITA"

def imprimeHorariosLaboratorios(matriz):
    for i in range(len(matriz)):
        print(f'{matriz[i][0]:<35} {matriz[i][1]:<30} {matriz[i][2]:<35} {matriz[i][3]:<36} {matriz[i][4]:<30}')

def exibeHorarioProfessor():
    for lab in range(len(geral)):
        for diaSemana in range(5):
            if nome in geral[lab][diaSemana]:
                aula = 0 if lab % 2 == 0 else 1
                horProf[aula][diaSemana] = geral[lab][diaSemana]
            else:
                pass

    print(f"{'Segunda':<34} {'Terça':<34} {'Quarta':<34} {'Quinta':<34} {'Sexta':<34}")
    for lab in range(len(horProf)):
        for diaSemana in range(5):
            print(f"{horProf[lab][diaSemana]:<34}",end=' ')
        print()


# imprimeHorariosLaboratorios(geral)
exibeHorarioProfessor()
