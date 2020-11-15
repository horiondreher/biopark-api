from flask import Flask
from flask_restful import Api

from resources.employee import EmployeeRegister
from resources.message import Message, MessageItem

#configuração da api rest
app = Flask(__name__)

#variaveis de configuração que serão alteradas para .env mais tarde
app.config.update(
    TESTING=True,
    DEBUG= True,
    FLASK_ENV='development',
    SECRET_KEY='biopark_key',
)
api = Api(app)

api.add_resource(EmployeeRegister, '/register')
api.add_resource(Message, '/msg')
api.add_resource(MessageItem, '/msg/<string:_id>')
# abre conexão do servidor na porta selecionada

if __name__ == '__main__':
    app.run(port = 5000)
