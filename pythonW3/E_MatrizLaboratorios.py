import pandas as pd

horarios={
    "segunda":["DAIVES-Algoritmos - CC", "DAIVES - Algoritmos - CC", "Sinclair-Design", "", "DANIEL - Arquitetura - CC", "DANIEL - Arquitetura-CC", "ROSEMARY- Projeto Digital-Engo", "Mariana Costa-Engcv - Topicos", "VALMIR-Design-", "Sinclair-Design", "Sebastiao-Sistemas - CC", "Sebastiao-Sistemas - CC", "BRUNO HENRIQUE-CC", "BRUNO HENRIQUE-CC", "RAUL CESAR - Algoritmos - CC", "RAUL CESAR - Algoritmos - CC"],
    "terca":["YURI Multimida - SI", "YURI-Logica - SI", "DANIEL - Arquitetura-CC", "DANIEL - Arquitetura -CC", "FABIO - ESTATÍSTICA -EngCV", "FABIO - ESTATÍSTICA -EngCV", "Sebastiao-Sistemas - CC", "Sebastiao-Sistemas - CC", "Sinclair-Design", "Sinclair - Design", "VALMIR-Design", "VALMIR-Design", "Marcos Antônio - EngPr", "Marcos Antônio - EngPr", "Fujita - Interface - CC", "RAUL CESAR - Logica- CC"],
    "quarta":["YURI-Imagens-CC", "YURI - Imagens-CC", "SAMARA - Simulação - EngQ", "","FABIO-ESTATÍSTICA -EngPr", "FABIO - ESTATÍSTICA -EngPr", "LUCAS SERAFIM-Sistemas - CC", "LUCAS SERAFIM-Sistemas - CC", "VALMIR-Design", "VALMIR-Design", "SANTACLARA - Algoritmos - CC", "SANTACLARA - Algoritmos - CC", "Fujita-Estrutura - CC", "Fujita-Estrutura - CC", "RAUL CESAR - Logica - CC", "TAGLIETTA-SO-CC"],
    "quinta":["VALMIR-Design", "Jose Ribeiro - Contabels", "DANIEL - Estrutura-CC", "DANIEL-Estrutura-CC", "FABIO-ALGEBRA -EngMo", "FABIO-ESTATÍSTICA -EngMc", "ROSEMARY- Projeto Digital-Engel", "ROSEMARY Projeto Digital - Engmec", "Sinclair - Design", "Sinclair - Design", "Paulo César - Estr Dados - Sl", "Paulo César-Estr Dados - SI", "SANTACLARA - Banco - Si", "SANTACLARA - Banco - SI", "Fujita - Arquitetura - SI", "TAGLIETTA-SO-CC"],
    "sexta":["Marcos Antônio - EngQui - Proje", "", "Laura Maria - TCC-EngPr", "Laura Maria-TCC-EngPr", "Mariana Costa - EngCv", "Mariana Costa - EngCv", "LUCAS SERAFIM-Sistemas -CC", "LUCAS SERAFIM-Sistemas - CC", "Laisa lemes-Design", "Laisa lemes - Design", "Sebastiao - Sistemas - CC", "Sebastiao-Sistemas - CC", "", "", "SANTACLARA - Banco - SI", "SANTACLARA - Banco-SI"]
}

df=pd.DataFrame(horarios)
segunda=df['segunda'].str.contains('Fujita')
terca=df['terca'].str.contains('Fujita')
quarta=df['quarta'].str.contains('Fujita')
quinta=df['quinta'].str.contains('Fujita')
sexta=df['sexta'].str.contains('Fujita')

print('segunda')
print(segunda,end=' ')
print('terca')
print(terca,end=' ')
print('quarta')
print(quarta,end=' ')
print('quinta')
print(quinta,end=' ')
print('sexta')
print(sexta,end=' ')