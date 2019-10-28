
import pyodbc 
import os


class Aluno():
    def __init__(self,nomeAluno,DtNascimentoAluno, idadeAluno,objetivoGraduacaoAluno, GeneroAluno, EmailAluno):
        self.nome = nomeAluno
        self.dtNascimento= DtNascimentoAluno
        self.idade= idadeAluno
        self.objetivoGraduacao= objetivoGraduacaoAluno
        self.genero= GeneroAluno
        self.email = EmailAluno
    def ListarPorEmai(self):
        server = 'DESKTOP-LJLFB93\SQLEXPRESS'
        database = 'CRUDPROF'
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
        cursor = cnxn.cursor()
        cursor.execute("SELECT Nome, Idade, Genero, DtNascimento, Email, ObjetivoGraduacao FROM Alunos where [Email] ='" + self.email + "'")
        result_set = cursor.fetchall()
        for row in result_set:
            print (row.Nome, ' | ' , row.Idade, ' | ' ,row.Genero, ' | ' ,row.DtNascimento, ' | ' ,row.Email, ' | ' ,row.ObjetivoGraduacao)
    def ListarTodos(self):
        server = 'DESKTOP-LJLFB93\SQLEXPRESS'
        database = 'CRUDPROF'
        conn = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;'
        cnxn = pyodbc.connect(conn)
        cursor = cnxn.cursor()
        cursor.execute("SELECT Nome, Email FROM Alunos")
        result_set = cursor.fetchall()#fetchall recebe o retorno do banco de dados...result-set uma variavel
        for row in result_set: #loop no banco de dados...
             print (row.Nome, ' | ' , row.Email)           
    def InserirUsuario(self):
        server = 'DESKTOP-LJLFB93\SQLEXPRESS'
        database = 'CRUDPROF'
        conn = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;'
        cnxn = pyodbc.connect(conn)
        cursor = cnxn.cursor()
        #para inserir como no BD... INSERT INTO VALUES E AS INFORMAÇÕES
        sql = "INSERT INTO Alunos (Nome,Idade,Genero,DtNascimento,Email,ObjetivoGraduacao) VALUES ('{}','{}','{}','{}','{}','{}')".format(self.nome,self.idade,self.genero,self.dtNascimento,self.email,self.objetivoGraduacao)
        cursor.execute(sql) 
        cursor.commit()
        cursor.close()
    def AlterarUsuario(self):
        server = 'DESKTOP-LJLFB93\SQLEXPRESS'
        database = 'CRUDPROF'
        conn = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;'
        cnxn = pyodbc.connect(conn)
        cursor = cnxn.cursor()
        sql = "UPDATE Alunos SET " #FAZENDO UPDATE NO BD...SQL NESSE CASO E UMA VARIAVEIL
        if (self.nome != ''):
            sql += "Nome = '{}', ".format(self.nome)
        if (self.idade != ""):
            sql += "Idade = {}, ".format(self.idade)
        if (self.dtNascimento != ""):
            sql += "DtNascimento = '{}', ".format(self.dtNascimento)
        if (self.objetivoGraduacao != ""):
            sql += "ObjetivoGraduacao = '{}', ".format(self.objetivoGraduacao)
        if (self.genero != ""):
            sql += "Genero = '{}', ".format(self.genero)
        sql = sql[:-2] #TIRNDO OS DOIS ULTIMO CARACTERE DA BASE DE DADOS
        sql += " WHERE email = '{}'".format(self.email)
        print (sql)#DICA FAZENDO UM PRINT DA QUERY PARA SABER COMO ESTA O FUNCIONAMENTO

        
        cursor.execute(sql) 
        cursor.commit()
        cursor.close()
    def DeletarUsuario(self):
        server = 'DESKTOP-LJLFB93\SQLEXPRESS'
        database = 'CRUDPROF'
        conn = 'DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;'
        cnxn = pyodbc.connect(conn)
        cursor = cnxn.cursor()
        sql = "DELETE Alunos WHERE Email = '{}'".format(self.email)
        cursor.execute(sql) 
        cursor.commit()#EFETOAR A TRANSAÇÃO NO BD
        cursor.close()

mensagem = "Digite uma opção \n1-Inserir \n2-Atualizar\n3-Excluir\n4-Listar por email\n5-Sair\n"
ret = int(input(mensagem))
while (ret != 5):
    if (ret==1):
        nome = input("Digite o nome ")
        dtnascimento = input("Digite a data de Nascimento ")
        idade = input("Digite o idade ")
        obetivoGraduacao = input("Digite o objetivo da graduação ")
        genero = input("Digite o Genero ")
        email = input("Digite o email ")
        objAluno = Aluno(nome,dtnascimento,idade,obetivoGraduacao, genero,email)
        objAluno.InserirUsuario()
        print('Usuaro inserido com sucesso')
    elif (ret==2):
        objAluno = Aluno("","","","","","")
        objAluno.ListarTodos()
        email = input("Digite o email que deseja alterar ")
        nome = input("Digite o nome (deixe em branco se não quiser alterar) ")
        dtnascimento = input("Digite a data de Nascimento (deixe em branco se não quiser alterar) ")
        idade = input("Digite o idade (deixe em branco se não quiser alterar) ")
        obetivoGraduacao = input("Digite a graduação (deixe em branco se não quiser alterar) ")
        genero = input("Digite o Genero (deixe em branco se não quiser alterar) ")
        objAluno = Aluno(nome,dtnascimento,idade,obetivoGraduacao, genero,email)
        objAluno.AlterarUsuario()
        print('Usuaro alterado com sucesso')
    elif (ret==3):
        objAluno = Aluno("","","","","","")
        objAluno.ListarTodos()
        email = input("Digite o email que deseja excluir ")
        objAluno = Aluno("","","","", "",email)
        if (input('Tem certeza que deseja excluir esse usuário? Essa ação não poderá ser desfeita (S/N)') == 'S'):
            objAluno.DeletarUsuario()
            print('Usuaro excluido com sucesso')
    elif (ret==4):
        email = input('Digite um email ')
        objAluno = Aluno("","","","","",email)
        objAluno.ListarPorEmai()

    ret = int(input (mensagem))
