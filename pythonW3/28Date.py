# Date → importar a biblioteca datetime
import datetime
print(datetime.datetime.now()) # 2024-07-29 22:43:45.186407
data = datetime.datetime.now()
print(data.year)
print(f'{data.day}/{data.month}/{data.year}')
print(data.strftime('%A'))

# Creating Date Objects
# data com ano, mês e dia
intake = datetime.datetime(2024,12,10) 
print(intake)

# The strftime() Method → Formata a data/hora de acordo com as especificações:
print(intake.strftime('%B'))

holyday = datetime.datetime(2024, 9, 7, 18, 15, 45)
print(holyday.strftime('%a')) # Sat
print(holyday.strftime('%A')) # Saturday
print(holyday.strftime('%w')) # 6 → 0 is sunday, 1 is monday and so on.
print(holyday.strftime('%d')) # 07 (dia)
print(holyday.strftime('%b')) # Sep
print(holyday.strftime('%B')) # September
print(holyday.strftime('%m')) # 09 (mês)
print(holyday.strftime('%y')) # 24 (ano com 2 dígitos)
print(holyday.strftime('%Y')) # 2024 (ano com 4 dígitos)
print(holyday.strftime('%H')) # 18 (hora) no formato 24h
print(holyday.strftime('%I')) # 6 (hora) no formato 12h
print(holyday.strftime('%p')) # PM
print(holyday.strftime('%M')) # 15 (minuto)
print(holyday.strftime('%S')) # 45 (segundos)
print(holyday.strftime('%f')) # 000000 (microssegundos)
print(holyday.strftime('%z')) #
print(holyday.strftime('%Z')) #
print(holyday.strftime('%j')) # 251 (dia do ano)
print(holyday.strftime('%U')) # 35 (semana do ano iniciando no domingo) 
print(holyday.strftime('%W')) # 36 (semana do ano iniciando na segunda)
print(holyday.strftime('%c')) # Sat Sep  7 18:15:45 2024 (versão da data e hora local)       
print(holyday.strftime('%C')) # Século
print(holyday.strftime('%x')) # 09/07/24
print(holyday.strftime('%X')) # 18:15:45