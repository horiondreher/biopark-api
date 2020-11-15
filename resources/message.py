from flask_restful import Resource,reqparse, inputs
from datetime import datetime

from models.message import MessageModel

class Message(Resource):

    # parser para validação de dados enviados pelo client
    parser = reqparse.RequestParser()

    # Nome completo, usuário e senha não podem ser deixados em branco.
    # O parser disponibilizado pelo flask será responsável por autenticar
    # o documento json enviado na requisição e retornará uma resposta 400 - bad request
    # se os parâmetros não forem cumpridos
    parser.add_argument('message_dt', type = inputs.datetime_from_iso8601, required = True, help = "Este campo não pode ser deixado em branco")
    parser.add_argument('sender_worker_id', type = int, required = True, help = "Este campo não pode ser deixado em branco")
    parser.add_argument('receiver_worker_id', type = int, required = True, help = "Este campo não pode ser deixado em branco")
    parser.add_argument('email', type = str, required = False, help = "Este campo não pode ser deixado em branco")
    parser.add_argument('phone', type = str, required = False, help = "Este campo não pode ser deixado em branco")
    parser.add_argument('message_app', type = str, required = False, help = "Este campo não pode ser deixado em branco")
    parser.add_argument('message', type = str, required = True, help = "Este campo não pode ser deixado em branco")

    def get(self, _id):
        pass
    
    def post(self):
        data = Message.parser.parse_args()
        
        msg = MessageModel(**data)
        msg.save_message()

    def delete(self, _id):
        pass
