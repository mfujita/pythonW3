import pandas as pd

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
horProf = []
nome="FUJITA"

def imprimeHorariosLaboratorios(matriz):
    for i in range(len(matriz)):
        print(f'{matriz[i][0]:<35} {matriz[i][1]:<30} {matriz[i][2]:<35} {matriz[i][3]:<36} {matriz[i][4]:<30}')

def preparaDados():
    for i in range(len(geral)):
        for j in range(5):
            if geral[i][j] != "":
                campo = geral[i][j].split('-')
                print(f"'lab': '{campo[0]}', 'nome': '{campo[1]:<14}', 'disciplina': '{campo[2]:<18}'")
            else:
                print(f"'lab': '    ', 'nome': '              ', 'disciplina': '                  '")

preparaDados()
        

# def exibeHorarioProfessor():
#     for dia in range(len(geral)):
#         for coluna in range(5):
#             if nome in geral[dia][coluna]:
                # horProf[dia][coluna] = geral[dia][coluna]
                # print(geral[dia][coluna], end=' ')
            # else:
            #     # horProf[dia][coluna] = ""
            #     print()

    # print(horProf)

# imprimeHorariosLaboratorios(geral)
# exibeHorarioProfessor()
# mat = exibeHorarioProfessor()

# def readJSON():
#     geral = {
#         "segunda": {
#              'lab': 'Lab1', 'nome':'DAIVES',         'disciplina':'Algoritmos',      'horario':'19:00 às 22:10'],
#             [ 'lab': 'Lab2', 'nome':'Sinclair',       'disciplina':'Design',          'horario':'19:00 às 20:30'],
#             [ 'lab': 'Lab3', 'nome':'DANIEL',         'disciplina':'Arquitetura',     'horario':'19:00 às 22:10'],
#             [ 'lab': 'Lab4', 'nome':'ROSEMARY',       'disciplina':'Projeto Digital', 'horario':'19:00 às 20:30'],
#             [ 'lab': 'Lab4', 'nome':'Mariana Costa',  'disciplina':'Engov',           'horario':'19:00 às 20:30'],
#             [ 'lab': 'Lab5', 'nome':'VALMIR',         'disciplina':'Design',          'horario':'19:00 às 20:30'],
#             [ 'lab': 'Lab5', 'nome':'Sinclair',       'disciplina':'Design',          'horario':'20:50 às 22:10'],
#             [ 'lab': 'Lab6', 'nome':'Sebastiao',      'disciplina':'Sistemas',        'horario':'19:00 às 22:10'],
#             [ 'lab': 'Lab7', 'nome':'BRUNO HENRIQUE', 'disciplina':'CC',              'horario':'19:00 às 22:10'],
#             [ 'lab': 'Lab8', 'nome':'RAUL CESAR',     'disciplina':'Algoritmos',      'horario':'19:00 às 22:10']
#         },
#         "terça": [
#             [ 'lab':'Lab1', 'nome':'DAIVES        ', 'disciplina':'Algoritmos     ' ],
#             [ 'lab':'Lab2', 'nome':'Sinclair      ', 'disciplina':'Design         ' ],
#             [ 'lab':'Lab3', 'nome':'DANIEL        ', 'disciplina':'Arquitetura    ' ],
#             [ 'lab':'Lab4', 'nome':'ROSEMARY      ', 'disciplina':'Projeto Digital' ],
#             [ 'lab':'Lab5', 'nome':'VALMIR        ', 'disciplina':'Design         ' ],
#             [ 'lab':'Lab6', 'nome':'Sebastiao     ', 'disciplina':'Sistemas       ' ],
#             [ 'lab':'Lab7', 'nome':'BRUNO HENRIQUE', 'disciplina':'CC             ' ],
#             [ 'lab':'Lab8', 'nome':'RAUL CESAR    ', 'disciplina':'Algoritmos     ' ]
#         ]
# }
    
#     df = pd.DataFrame(geral)
#     print(df['segunda'])

# readJSON()