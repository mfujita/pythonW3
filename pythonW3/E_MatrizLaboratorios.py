import pandas as pd

horarios={
    "segunda":["DAIVES-Algoritmos - CC", "DAIVES - Algoritmos - CC", "Sinclair-Design", "", "DANIEL - Arquitetura - CC", "DANIEL - Arquitetura-CC", "ROSEMARY- Projeto Digital-Engo", "Mariana Costa-Engcv - Topicos", "VALMIR-Design-", "Sinclair-Design", "Sebastiao-Sistemas - CC", "Sebastiao-Sistemas - CC", "BRUNO HENRIQUE-CC", "BRUNO HENRIQUE-CC", "RAUL CESAR - Algoritmos - CC", "RAUL CESAR - Algoritmos - CC"],
    "terca":["YURI Multimida - SI", "YURI-Logica - SI", "DANIEL - Arquitetura-CC", "DANIEL - Arquitetura -CC", "FABIO - ESTATÍSTICA -EngCV", "FABIO - ESTATÍSTICA -EngCV", "Sebastiao-Sistemas - CC", "Sebastiao-Sistemas - CC", "Sinclair-Design", "Sinclair - Design", "VALMIR-Design", "VALMIR-Design", "Marcos Antônio - EngPr", "Marcos Antônio - EngPr", "Fujita - Interface - CC", "RAUL CESAR - Logica- CC"],
    "quarta":["YURI-Imagens-CC", "YURI - Imagens-CC", "SAMARA - Simulação - EngQ", "","FABIO-ESTATÍSTICA -EngPr", "FABIO - ESTATÍSTICA -EngPr", "LUCAS SERAFIM-Sistemas - CC", "LUCAS SERAFIM-Sistemas - CC", "VALMIR-Design", "VALMIR-Design", "SANTACLARA - Algoritmos - CC", "SANTACLARA - Algoritmos - CC", "Fujita-Estrutura - CC", "Fujita-Estrutura - CC", "RAUL CESAR - Logica - CC", "TAGLIETTA-SO-CC"],
    "quinta":["VALMIR-Design", "Jose Ribeiro - Contabels", "DANIEL - Estrutura-CC", "DANIEL-Estrutura-CC", "FABIO-ALGEBRA -EngMo", "FABIO-ESTATÍSTICA -EngMc", "ROSEMARY- Projeto Digital-Engel", "ROSEMARY Projeto Digital - Engmec", "Sinclair - Design", "Sinclair - Design", "Paulo César - Estr Dados - Sl", "Paulo César-Estr Dados - SI", "SANTACLARA - Banco - Si", "SANTACLARA - Banco - SI", "Fujita - Arquitetura - SI", "TAGLIETTA-SO-CC"],
    "sexta":["Marcos Antônio - EngQui - Proje", "", "Laura Maria - TCC-EngPr", "Laura Maria-TCC-EngPr", "Mariana Costa - EngCv", "Mariana Costa - EngCv", "LUCAS SERAFIM-Sistemas -CC", "LUCAS SERAFIM-Sistemas - CC", "Laisa lemes-Design", "Laisa lemes - Design", "Sebastiao - Sistemas - CC", "Sebastiao-Sistemas - CC", "", "", "SANTACLARA - Banco - SI", "SANTACLARA - Banco-SI"]
}

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

def preparaDados():
    for i in range(len(geral)):
        for j in range(5):
            if geral[i][j] != "":
                campo = geral[i][j].split('-')
                if j == 0:
                    print(f"'lab': '{campo[0]}', 'nome': '{campo[1]:<14}', 'disciplina': '{campo[2]:<18}', 'dia':'segunda'")
                if j == 1:
                    print(f"'lab': '{campo[0]}', 'nome': '{campo[1]:<14}', 'disciplina': '{campo[2]:<18}', 'dia':'terça'")
                if j == 2:
                    print(f"'lab': '{campo[0]}', 'nome': '{campo[1]:<14}', 'disciplina': '{campo[2]:<18}', 'dia':'quarta'")
                if j == 3:
                    print(f"'lab': '{campo[0]}', 'nome': '{campo[1]:<14}', 'disciplina': '{campo[2]:<18}', 'dia':'quinta'")
                if j == 4:
                    print(f"'lab': '{campo[0]}', 'nome': '{campo[1]:<14}', 'disciplina': '{campo[2]:<18}', 'dia':'sexta'")
            # else:
            #     print(f"'lab': '    ', 'nome': '              ', 'disciplina': '                  '")
            

preparaDados()