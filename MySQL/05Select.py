# Select
import mysql.connector
db1=mysql.connector.connect(
    host='localhost',
    user='root',
    password='daskiblou1!',
    database='mydatabase'
)

mycursor=db1.cursor()
# mycursor.execute("SELECT * FROM cadastropessoas")
mycursor.execute("SELECT id, nome, nota1 from cadastropessoas")
# result=mycursor.fetchall() # o método fetchall() produz todas as linhas da última instrução
result=mycursor.fetchone()
for x in result:
    print(x)

# Using the fetchone() Method → retorna a primeira linha do resultado