# Como expressar a data do formato do Brasil
import datetime
dia = str(datetime.datetime.now()).split(' ')[0].split('-')[2]
mes = str(datetime.datetime.now()).split(' ')[0].split('-')[1]
ano = str(datetime.datetime.now()).split(' ')[0].split('-')[0]
print(dia+"/"+mes+"/"+ano)

