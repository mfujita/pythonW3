# Como expressar a data do formato do Brasil
import datetime
dia = str(datetime.datetime.now()).split(' ')[0].split('-')[2]
mes = str(datetime.datetime.now()).split(' ')[0].split('-')[1]
ano = str(datetime.datetime.now()).split(' ')[0].split('-')[0]
print(dia+"/"+mes+"/"+ano)

dataString = ['05/09/2024', '01/09/2024', '20/08/2024', '17/09/2024', '14/09/2024', '03/09/2024', '11/09/2024']
myDate = []

for i in range(len(dataString)):
    dia=int(dataString[i].split('/')[0])
    mes=int(dataString[i].split('/')[1])
    ano=int(dataString[i].split('/')[2])
    myDate.append(datetime.date(ano, mes, dia))

myDate.sort()
for item in myDate:
    print(item)