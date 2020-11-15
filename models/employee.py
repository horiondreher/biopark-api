import mysql.connector
from mysql.connector import errorcode 

from config import db_connect

class EmployeeModel():
    TABLE_NAME = 'employee'

    # variaveis necessárias para tabela de usuarios cadastrados
    def __init__(self, worker_id, fullname, username, password):
        self.worker_id = worker_id
        self.fullname = fullname
        self.username = username
        self.password = password

    # Método utilizado para salvar um novo usuário no banco de dados.
    # A partir de uma classe com as variáveis corretas validadas pelo parser
    # uma  query é criada e executada pelo MySQL connector utilizando o cursor
    # qualquer erro interno é retornado com o código 500 - INTERNAL SERVER ERROR
    def save_employee(self):
        query = ("INSERT INTO employee" 
                "(worker_id, full_name, username, password)"
                "VALUES (%s, %s, %s, %s)")
        data_employee = (self.worker_id, self.fullname, self.username, self.password)
        
        try:
            cnx = mysql.connector.connect(**db_connect) # cnx armazena o objeto de conexão
            cursor = cnx.cursor() # cursor é o objeto usado para querys
            cursor.execute(query, data_employee)
        except mysql.connector.Error as err:
            print(err)
        
        # fecha cursos e conexão com banco de dados
        cursor.close()
        cnx.close()
        return {'message': 'Usuário cadastrado com sucesso'}
    

    # Métodos criado para facilitar a busca de usuário por nome e ID
    # Caso não encontre, retorna um resultado nulo
    @classmethod
    def find_employee_username(cls, username):
        query = ("SELECT * FROM {} WHERE username=%s".format(cls.TABLE_NAME))

        try:
            cnx = mysql.connector.connect(**db_connect) # cnx armazena o objeto de conexão
            cursor = cnx.cursor() # cursor é o objeto usado para querys
            cursor.execute(query, (username,))
            row = cursor.fetchone()
        except mysql.connector.Error as err:
            print(err)

        if row:
            user = cls(*row)
        else:
            user = None    
        # fecha cursos e conexão com banco de dados
        cursor.close()
        cnx.close()

        return user
    
    @classmethod
    def find_employee_worker_id(cls, worker_id):
        query = ("SELECT * FROM {} WHERE worker_id=%s".format(cls.TABLE_NAME))

        try:
            cnx = mysql.connector.connect(**db_connect) # cnx armazena o objeto de conexão
            cursor = cnx.cursor() # cursor é o objeto usado para querys
            cursor.execute(query, (worker_id,))
            row = cursor.fetchone()
        except mysql.connector.Error as err:
            print(err)

        if row:
            _id = cls(*row)
        else:
            _id = None    
        # fecha cursos e conexão com banco de dados
        cursor.close()
        cnx.close()

        return _id
