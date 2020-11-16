# biopark-api
API desenvolvida em python para o processo seletivo do trainee Biopark.

A API consiste de uma aplicação em Python e um banco de dados em MYSQL.
O programa em Python é composto principalmente por Flask-RESTful e
MySQL-connector, ferramentas necessárias para atingir o resultado final esperado.

## Instalação

**Para a execução deste projeto foi utilizado um sistema Linux.**

Para executar o projeto corremente será necessário:
1. Instalar o banco de dados MySQL
1. Instalar as dependências em python listados em `requirements.txt`
1. Executar o script em python `create_db.py` para criação do BD e suas tabelas

Supondo que o MySQL esteja instalado, utilizando python3, instale as dependências com:

`pip install -r requirements.txt`

Isto instalará todas as dependências necessárias para execução do projeto.
Para criar o *database* e suas tabelas, configure o arquivo `config.py`, com as informações do sistema e execute:

`python create_db.py`

## Funcionamento da API

A API foi desenvolvida com a utilização do framwork Flask, 
escolhido pela sua abrangente utilização. 
Seu objetivo é enviar mensagens a partir de um agendamento, 
utilizando o meio de comunicação escolhido pelo usuário, 
seja email, sms, push ou Whatsapp.

### Banco de dados
Para isto, foram criadas duas tabelas no banco de 
dados ('messages'): de funcionário ('employee'), 
que define quem está enviando e quem receberá a mensagem, 
e a de mensagens ('msgs'), que armazenará as informações 
necessárias para envio.

As tabela employee é formada por:

Coluna        | Type         
------------ | -------------
worker_id | int unsigned
full_name | varchar(64)
username  | varchar(32)
password  | varchar(32)

E a tabela msgs é formada por:

| Field              | Type
------------ | -------------
| dt                 | datetime     
| message_id         | int          
| message_dt         | datetime          
| sender_worker_id   | int unsigned 
| receiver_worker_id | int unsigned 
| email              | varchar(32)
| phone              | varchar(32) 
| message_app        | varchar(32) 
| message            | mediumtext 

### Endpoints

A API possui 4 endpoints:

* /register - POST - realiza o registro do usuário
* /msg - POST -  realiza o cadastro da mensagem com POST
* /msg/id - GET - realiza a consulta de mensagens por id do usuário
* /msg/id - DELETE - realiza a remoção de mensagen por id de mensagem

Para criar uma mensagem, o sistema precisa ter o cadastro 
do remetente e destinatário, para isto o cadastro é 
realizado em /register com o envio de um documento JSON, como no exemplo:

```json
{
    "worker_id": "101",
    "fullname": "Horion Silva Dreher",
    "username": "horiondreher",
    "password": "123456"
}
```

Com isso, para armazenar a mensagem, é necessário enviar 
um documento JSON para /msg, como:

```json
{
    "message_dt": "2020-11-14T23:00:00-03:00",
    "sender_worker_id": "100",
    "receiver_worker_id": "101",
    "email": null,
    "phone": null,
    "message_app": null,
    "message": "Mensagem a ser enviada"
}
```
Para consultar as mensagens agendadas de um usuário, deve-se
utilizar, por exemplo, `/msg/100`, para obter todas as mensagens
do funcionário com o ID de cadastro *100*.

Da mesma forma, para deletar uma mensagem agendada, deve-se
utilizar, por exemplo `/msg/1`, para deletar a mensagem com o ID *1*

Por fim, para a execução da API, utilizar

`python app.py`

## Melhorias

A API ainda apresenta recursos que podem ser melhorados, para 
aumentar a qualidade de comunicação entre *client* e *server*.

Uma delas é utilizar autenticação com JWT, para validar usuários e
permitir que o servidor não precise armazenar a sessão, mas, apenas
que receba a chave de autenticação.

Outra melhoria é melhorar a dinâmica de mensagens criadas, pois a 
forma de envio ainda não foi bem desenvolvida.

Por fim, criar variáveis de ambiente, para melhorar a dinâmica
de um programa em desenvovimento ou produção, e assim, não utilizar
variáveis dentro do código, o que pode prejudicar o resultado.
