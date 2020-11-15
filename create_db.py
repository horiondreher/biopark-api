import mysql.connector
from mysql.connector import errorcode

# configurações para o BD de teste
config = {
    'user': 'root',
    'password': '123456QwE*',
    'host': '127.0.0.1',
    'raise_on_warnings': True
}

# utilizando o mysql.connector, passo as informações necessárias para conexão local ao MySQL
try:
    cnx = mysql.connector.connect (**config)
    print("Conexão realizada com sucesso")
except mysql.connector.Error as err: # tratamento de erros com códigos disponibilizados por "errorcode"
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nome ou senha incorretos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    else:
        print(err)
else:
    cnx.close()
