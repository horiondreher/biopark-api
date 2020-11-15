import mysql.connector
from mysql.connector import errorcode 

from config import db_connect

class EmployeeModel():
    TABLE_NAME = 'employee'

    def __init__(self, worker_id, fullname, username, password):
        self.worker_id = worker_id
        self.fullname = fullname
        self.username = username
        self.password = password

    def save_employee(self):
        query = ( "INSERT INTO employee" 
                "(worker_id, full_name, username, password)"
                "VALUES (%s, %s, %s, %s)")
        data_employee = (self.worker_id, self.fullname, self.username, self.password)
        
        try:
            cnx = mysql.connector.connect(**db_connect) # cnx armazena o objeto de conexão
            cursor = cnx.cursor() # cursor é o objeto usado para querys
            cursor.execute(query, data_employee)
        except mysql.connector.Error as err:
            print(err)
            return 400
        
        # fecha cursos e conexão com banco de dados
        cursor.close()
        cnx.close()
        return 201