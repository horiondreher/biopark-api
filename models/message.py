import mysql.connector
from mysql.connector import errorcode 

from config import db_connect

class MessageModel():
    TABLE_NAME = 'msgs'

    def __init__(self, message_dt, sender_worker_id, receiver_worker_id,
                email, phone, message_app, message):
        self.message_dt = message_dt
        self.sender_worker_id = sender_worker_id
        self.receiver_worker_id = receiver_worker_id
        self.email = email
        self.phone = phone
        self.message_app = message_app
        self.message = message
    
    def save_message(self):
        query = ("INSERT INTO {}" 
                "(message_dt, sender_worker_id, receiver_worker_id, email, phone, message_app, message)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s)".format(self.TABLE_NAME))
        data_employee = (self.message_dt, self.sender_worker_id, self.receiver_worker_id, 
                        self.email, self.phone, self.message_app, self.message)
        
        try:
            cnx = mysql.connector.connect(**db_connect) # cnx armazena o objeto de conexão
            cursor = cnx.cursor() # cursor é o objeto usado para querys
            cursor.execute(query, data_employee)
        except mysql.connector.Error as err:
            print(err)
        
        # fecha cursos e conexão com banco de dados
        cursor.close()
        cnx.close()
