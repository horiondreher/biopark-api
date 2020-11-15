import mysql.connector

cnx = mysql.connector.connect(
    user = 'root',
    password = '123456QwE*',
    host = '127.0.0.1'
)

cnx.close()
