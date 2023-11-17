import mysql.connector


banco = mysql.connector.connect(
     host="localhost",
     user="root",
     password="302302",
     database="academia"
      )

cursor =banco.cursor()


def ler(opcao):
    match opcao:
        case 1:
            tabela = "alunos"
        case 2:
            tabela = "funcionarios"
        case 3:
            tabela = "personal"
        case 4:
            tabela = "modalidade"
        case _:
            print("Opcao invalida, por favor tente novamente")

    pesquisa = f'select * from {tabela};'
    cursor.execute(pesquisa)
    resultado= cursor.fetchall()
    for i in resultado:
        print(i)

def criar(opcao):

    match opcao:
        case 1:
            print("======INSERIR ALUNO======")
            nome = input("Digite o seu nome: ")
            while not nome.replace(" ","").isalpha():
                nome = input("Nome invalido, digite algo valido: ")
            cpf = input("Digite seu cpf")
            while len(cpf) != 11 or cpf.isalpha():
                cpf = input("Cpf invalido, digite algo valido: ")
            telefone = input("Digite o seu telefone: ")
            while len(telefone) != 11 or telefone.isalpha():
                telefone = input("telefone invalido, digite algo valido: ")
            endereco = input("Digite seu endereco: ")
            while not endereco.replace(" ","").isascii():
                endereco = input("endereco invalido, digite algo valido: ")

            inserir = "INSERT INTO alunos(nome,cpf,telefone,endereco) values (%s,%s,%s,%s) "
            dados = (nome,cpf,telefone,endereco)
            cursor.execute(inserir,dados)
            banco.commit()
            print("o novo aluno foi inserido com sucesso")
        case 2:
            print("======INSERIR FUNCIONARIO======")
            nome = input("Digite o seu nome: ")
            while not nome.replace(" ","").isalpha():
                nome = input("Nome invalido, digite algo valido: ")
            cpf = input("Digite seu cpf")
            while len(cpf) != 11 or cpf.isalpha():
                cpf = input("Cpf invalido, digite algo valido: ")
            departamento = input("Digite o seu departamento: ")
            while departamento.isalpha():
                departamento = input("departamento invalido, digite algo valido: ")
            salario = float(input("Digite o seu salario: "))
            while not salario.is_integer():
                salario = input("salario invalido, digite algo valido: ")
            email = input("Digite o seu email: ")
            while "@" not in email:
                email = input("email invalido, digite algo valido: ")
            endereco = input("Digite seu endereco: ")
            while not endereco.replace(" ","").isascii():
                endereco = input("endereco invalido, digite algo valido: ")

            inserir = "INSERT INTO funcionarios(nome,cpf,departamento,salario,email,enderoco) values (%s,%s,%s,%s,%s,%s) "
            dados = (nome,cpf,departamento,salario,email,endereco)
            cursor.execute(inserir,dados)
            banco.commit()


def deletar(opcao):
    match opcao:
        case 1:
            id= int(input("quem voce deseja excluir da tabela(pelo id)"))
            deletarDados = f"DELETE FROM alunos where matricula = {id}"
            cursor.execute(deletarDados)
            banco.commit()
            print("deletado")
        case 2:
            id= int(input("quem voce deseja excluir da tabela(pelo id)"))
            deletarDados = f"DELETE FROM Funcionarios where id_funcionario = {id}"
            cursor.execute(deletarDados)
            banco.commit()
            print("deletado")

        case 3:
            id= int(input("quem voce deseja excluir da tabela(pelo id)"))
            deletarDados = f"DELETE FROM Modalidades where id_modalidade = {id}"
            cursor.execute(deletarDados)
            banco.commit()
            print("deletado")

        case 4:
            id= int(input("quem voce deseja excluir da tabela(pelo id)"))
            deletarDados = f"DELETE FROM Personal where id_personal = {id}"
            cursor.execute(deletarDados)
            banco.commit()
            print("deletado")
        case _:
            print("opcao invalida")

def editar(opcao):
    if opcao == 1:
        mudar = input("oq vc deseja mudar? nome cpf telefone ")
        novo_valor= input("Qual o novo dado?")
        id=input("qual o id do aluno?")
        editarDados = f"UPDATE alunos SET {mudar}='{novo_valor}' WHERE matricula= {id}"
        cursor.execute(editarDados)
        banco.commit()

editar(1)

