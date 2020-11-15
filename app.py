from flask import Flask
from flask_restful import Api

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

# abre conexão do servidor na porta selecionada
app.run(port = 5000)
