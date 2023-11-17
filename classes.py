import mysql.connector

class Banco:
    def __init__(self, host,user,password,database):
        self.host= host,
        self.user=user,
        self.password=password,
        self.database=database


    def criarBanco(self):
        banco = mysql.connector.connect(
            host=self.host,
            user=self.host,
            password=self.password,
            database=self.database
        )
        cursor = banco.cursor()






