import mysql.connector

db1=mysql.connector.connect(
    host="localhost",
    user="root",
    password="1!2@3#4$",

)

mycursor=db1.cursor()
# mycursor.execute("CREATE DATABASE bancodados")
mycursor.execute("USE bancodados")
# mycursor.execute("CREATE TABLE pessoa (id int AUTO_INCREMENT PRIMARY KEY, nome varchar(30), nota1 float(2,1))")

# sql="INSERT INTO pessoa (nome, nota1) VALUES (%s,%s)"
# val=[
#     ('Tião', 4.2),
#     ('Kika', 2.7),
#     ('Petronio', 7.8),
#     ('Luchenko', 5.9),
#     ('Vlatormo', 4.6),
#     ('Espirinto', 9.0),
#     ('Jeguenildo', 0.4)
# ]

# mycursor.executemany(sql, val)
# db1.commit()
# print(mycursor.rowcount, "linhas inseridas.")

sql="UPDATE pessoa SET nota1 = 0.3 WHERE id = 7"
mycursor.execute(sql)
db1.commit()
print(mycursor.rowcount, " linha afetada.")