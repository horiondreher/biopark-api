import mysql.connector
from mysql.connector import errorcode

from config import db_config #arquivo de configuração

DB_NAME = 'messages'
TABLES = {}

# tabela de funcionário
# conterá informações básicas necessárias para identificar remetente e
# permitir o envio de mensagem apenas por pessoas cadastradas no sistema
TABLES['employee'] = (
    "CREATE TABLE employee (" 
    "worker_id INT UNSIGNED NOT NULL," # cadastro do funcionário que deverá ser único
    "full_name VARCHAR(64) NOT NULL," # nome completo do funcionário
    "username VARCHAR(32) NOT NULL," # username do funcionário
    "password VARCHAR(32) NOT NULL," # senha (deverá ser encriptada no futuro)
    "PRIMARY KEY (worker_id)," 
    "UNIQUE KEY (username)" 
    ") ENGINE=MyISAM" # engine escolhida para tabela devido a boa funcionalidade para poucas atualizações (mais simples)
)

# tabela de mensagens
# armazenará as informações necessarias para envio e consulta
# a mensagem será armazenada com o conteúdo, remetente, destinatário e horario de envio
# além disso, deverár conter as informações sobre qual método de envio será utilizado, tais como email ou sms.
# seu identificador será relacionado com a tabela de usuário, até porque, não pode ficar sem dono
TABLES['msgs'] = (
    "CREATE TABLE msgs ("
    "dt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP," # horário de criação
    "message_id INT NOT NULL AUTO_INCREMENT," # identificador único
    "message_dt DATETIME NOT NULL," # horário e data para envio
    "sender_worker_id INT UNSIGNED NOT NULL," # id de remetente, relacionado com tabela employee
    "receiver_worker_id INT UNSIGNED NOT NULL," # id de destinatário
    "email VARCHAR(32) DEFAULT NULL," # email para envio com identificador unico para tabela
    "phone VARCHAR(32) DEFAULT NULL," # telefone para envio de sms ou whastapp com identificador unico para tabela
    "message_app VARCHAR(32) DEFAULT NULL," # meio de envio que será utilizado
    "message MEDIUMTEXT DEFAULT NULL," # conteúdo da mensagem
    "PRIMARY KEY (message_id)," 
    "UNIQUE KEY email (email),"
    "UNIQUE KEY phone (phone),"
    "FOREIGN KEY (sender_worker_id) REFERENCES employee(worker_id)"
    ") ENGINE=MyISAM"
)

# utilizando o mysql.connector, passo as informações necessárias para conexão local ao MySQL
try:
    cnx = mysql.connector.connect(**db_config) # cnx armazena o objeto de conexão
    cursor = cnx.cursor() # cursor é o objeto usado para querys
    print("Conexão realizada com sucesso")
except mysql.connector.Error as err: # tratamento de erros com códigos disponibilizados por "errorcode"
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Nome ou senha incorretos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe")
    else:
        print(err)

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'UTF8MB4'".format(DB_NAME)) # criação do banco de dados
    except mysql.connector.Error as err: # se já existir ou possuir outro erro, retorna uma exception
        print("Falha na criação do banco de dados: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME)) # passa a utilizar o banco de dados escolhido
    print("Utilizando o banco de dados {}".format(DB_NAME))
except mysql.connector.Error as err: 
    print("O Banco de dados {} não existe".format(DB_NAME)) 
    if err.errno == errorcode.ER_BAD_DB_ERROR: # se o banco de dados não existir, chama o método create_database() para sua criação
        create_database(cursor)
        print("O Banco de dados {} foi criado com sucesso".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES: # cria uma iteração sobre as tabelas descritas acima
    table_description = TABLES[table_name]  # armazena a query
    try:
        print("Criando tabela {}: ".format(table_name), end='')
        cursor.execute(table_description) # executa as querys para criação
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR: # retorna exeption se tabela já existe a não realiza nenhuma ação
            print("já existe")
        else:
            print(err.msg)
    else:
        print("Ok") # se tudo ocorrer bem, imprime mensagem de ok, e partimos para o abraço

# fecha cursos e conexão com banco de dados
cursor.close()
cnx.close()
