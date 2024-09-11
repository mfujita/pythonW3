# insert
'''
import mysql.connector
db1=mysql.connector.connect (
    host='localhost',
    user='root',
    password='daskiblou1!',
    database='mydatabase'
)

mycursor=db1.cursor()
sql="INSERT INTO cadastropessoas (nome, nota1) VALUES (%s, %s)"
valores=("Chico Tico", 6.2)
mycursor.execute(sql, valores)
db1.commit()
print(mycursor.rowcount, "Registro inserido.")
'''

# Insert Multiple Rows
import mysql.connector
db1=mysql.connector.connect (
    host='localhost',
    user="root",
    password='daskiblou1!',
    database='mydatabase'
)

mycursor = db1.cursor()
'''
sql='INSERT INTO cadastropessoas (nome, nota1) VALUES (%s, %s)'
val = [
    ('Tião', 4.2),
    ('Kika', 2.7),
    ('Petronio', 7.8),
    ('Luchenko', 5.9),
    ('Vlatormo', 4.6),
    ('Espirinto', 9.0),
    ('Jeguenildo', 0.4)
]
mycursor.executemany(sql, val)
db1.commit()
print(mycursor.rowcount, "registros foram inseridos.") # 7 registros foram inseridos.
'''

# Get Inserted ID
# Se forem inseridos mais de uma linha, o último id será retornado.

sql="insert into cadastropessoas (nome, nota1) VALUES (%s, %s)"
val=[
    ('Huguinho', 1),
    ('Zezinho', 2),
    ('Luisinho', 3)
]
mycursor.executemany(sql, val)
db1.commit()
print("ID do lote inserido no banco de dados: ", mycursor.lastrowid)