# Where
'''
import mysql.connector
db1= mysql.connector.connect(
    host='localhost',
    user='root',
    password='daskiblou1!',
    database='mydatabase'
)
mycursor=db1.cursor()
sql="SELECt * FROM cadastropessoas where nome = 'Luchenko'"
mycursor.execute(sql)
result=mycursor.fetchall()
for item in result:
    print(item)
'''

# Prevent SQL Injection
import mysql.connector
db1=mysql.connector.connect(
    host='localhost',
    user='root',
    password='daskiblou1!',
    database='mydatabase'
)
mycursor = db1.cursor()
sql="SELECT * from cadastropessoas where nome = %s"
nome=("Luchenko",)
mycursor.execute(sql, nome)
result=mycursor.fetchall()

for item in result:
    print(item)