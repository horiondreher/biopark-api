import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'messages'
TABLES = {}

TABLES['employee'] = (
    " CREATE TABLE users ( "
    " worker_id int(16) unsigned NOT NULL, "
    " name varchar(32) NOT NULL, "
    " password varchar(32) NOT NULL, "
    " email varchar(32) NOT NULL, "
    " PRIMARY KEY (worker_id), "
    " UNIQUE KEY email (email) "
    " ) ENGINE=MyISAM"
)

TABLES['messages'] = (
    " CREATE TABLE messages ( "
    " dt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
    " message_id int(16) unsigned NOT NULL, "
    " message_dt DATETIME NOT NULL, "
    " sender_worker_id int(16) NOT NULL, "
    " receiver_worker_id int(16) NOT NULL, "
    " email varchar(32) DEFAULT NULL, "
    " phone varchar(32) DEFAULT NULL, "
    " message varchar DEFAULT NULL, "
    " message_app varchar DEFAULT NULL, "
    " PRIMARY KEY (message_id), "
    " UNIQUE KEY email (email), "
    " FOREIGN KEY (sender_worker_id) REFERENCES users(worker_id) "
    " ) ENGINE=MyISAM"
)

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
    cursor = cnx.cursor()
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

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Falha na criação do banco de dados: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("O Banco de dados {} não existe".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("O Banco de dados {} foi criado com sucesso".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)
        
