import mysql.connector
from funcoes import *
from classes import Banco

# banco = mysql.connector.connect(
#      host="localhost",
#      user="root",
#      password="302302",
#      database="academia"
#       )
# meucursor =banco.cursor()
#
# print(teste)
#
# pesquisa = f'select * from funcionarios;'
#
# meucursor.execute(pesquisa)
# resultado= meucursor.fetchall()
#
# for i in resultado:
#     print(i)

# nome1="menino Ney"
# cpf="111111111"
# dep = "1"
# salario = 5440.00
# email="pl@luc.com"
# enderoco="rua 1"
#
# cursor = banco.cursor()
#
# sql = "INSERT INTO funcionarios(nome, CPF, departamento,salario,email,enderoco) VALUES (%s,%s,%s,%s,%s,%s)"
# data = ( nome1, cpf, dep,salario,email,enderoco)
# cursor.execute(sql, data)
# banco.commit()
# userid = cursor.lastrowid
# print(userid)


opcao = int
