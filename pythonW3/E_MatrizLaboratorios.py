import pandas as pd

geral = [
    ["Lab1-prof1", "Lab1-prof2", "Lab1-prof2", "Lab1-prof3", "Lab1-prof4"],
    ["Lab1-prof1", "Lab1-prof2", "Lab1-prof2", "Lab1-prof5", ""],
    ["Lab2-prof6", "Lab2-prof7", "Lab2-prof8", "Lab2-prof7", "Lab2-prof9"],
    ["          ", "Lab2-prof7", "          ", "Lab2-prof7", "Lab2-prof9"],
    ["Lab3-prof7", "Lab3-prof10", "Lab3-prof10", "Lab3-prof10", "Lab3-prof14"],
    ["Lab3-prof7", "Lab3-prof10", "Lab3-prof10", "Lab3-prof10", "Lab3-prof14"],
    ["Lab4-prof11", "Lab4-prof12", "Lab4-prof13", "Lab4-prof11", "Lab4-prof13"],
    ["Lab4-prof14", "Lab4-prof12", "Lab4-prof13", "Lab4-prof11", "Lab4-prof13"],
    ["Lab5-prof3", "Lab5-prof6", "Lab5-prof3", "Lab5-prof6", "Lab5-prof18"],
    ["Lab5-prof6", "Lab5-prof6", "Lab5-prof3", "Lab5-prof6", "Lab5-prof18"],
    ["Lab6-prof12", "Lab6-prof3", "Lab6-prof15", "Lab6-prof20", "Lab6-prof12"],
    ["Lab6-prof12", "Lab6-prof3", "Lab6-prof15", "Lab6-prof20", "Lab6-prof12"]
]

def imprimeHorariosLaboratorios(matriz):
    for i in range(len(matriz)):
        print(f'{matriz[i][0]:<10} {matriz[i][1]:<10} {matriz[i][2]:<10} {matriz[i][3]:<10} {matriz[i][4]:<10}')

def exibeHorarioProfessor(matriz):
    horProf = [] # [['','','','',''],['','','','','']]
    aula=0
    nome='prof12' # input('Nome do professor: ')

    for i in range(len(matriz)):
        # if i % 2 == 0: aula = 0 
        # else: aula = 1
        if nome in matriz[i][0]:
            # print(f"{matriz[i][0]:<12}")
            horProf[0] = matriz[i][0]
        # print(f"{matriz[i][0]:<12} {matriz[i][1]:<12} {matriz[i][2]:<12} {matriz[i][3]:<12} {matriz[i][4]:<12}")
        # if nome in matriz[i][0]:

        #     horProf[aula][0] = matriz[i][0]
        # elif nome in matriz[i][1]:

        #     horProf[aula][1] = matriz[i][1]
        # elif nome in matriz[i][2]:

        #     horProf[aula][2] = matriz[i][2]
        # elif nome in matriz[i][3]:

        #     horProf[aula][3] = matriz[i][3]
        # elif nome in matriz[i][4]:

        #     horProf[aula][4] = matriz[i][4]

    print(horProf)

    # for linha in range(len(geral)):
    #     for coluna in range(len(linha)):
    #         print(f'{geral}[{linha}][{coluna}] ', end=' ')
    #     print()

    # for dia in range(len(horProf)):
    #     for coluna in range(len(horProf)):
    #         if nome in coluna:
    #             horProf[dia][periodo] += geral[coluna]
    #         else:
    #             horProf[dia][periodo] += ''
    #     #     print(f"{coluna:<3}", end=' ')
    #     # print()
    # print(horProf)

# imprimeHorariosLaboratorios(geral)
exibeHorarioProfessor(geral)
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