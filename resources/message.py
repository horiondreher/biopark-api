from flask_restful import Resource, reqparse, inputs

from datetime import datetime
import pytz

from models.employee import EmployeeModel
from models.message import MessageModel
class Message(Resource):

    # parser para validação de dados enviados pelo client
    parser = reqparse.RequestParser()

    # Data e hora de envio, usuário destino e mensagem não podem ser deixados em branco.
    # O parser disponibilizado pelo flask será responsável por autenticar
    # o documento json enviado na requisição e retornará uma resposta 400 - BAD REQUEST
    # se os parâmetros não forem cumpridos
    parser.add_argument('message_dt', type = inputs.datetime_from_iso8601, required = True, help = "Este campo não pode ser deixado em branco")
    parser.add_argument('sender_worker_id', type = int, required = True, help = "Este campo não pode ser deixado em branco")
    parser.add_argument('receiver_worker_id', type = int, required = True, help = "Este campo não pode ser deixado em branco")
    parser.add_argument('email', type = str, required = False)
    parser.add_argument('phone', type = str, required = False)
    parser.add_argument('message_app', type = str, required = False)
    parser.add_argument('message', type = str, required = True, help = "Este campo não pode ser deixado em branco")


    # Metodo POST para mensagens
    # Utiliza todas as informações necessarias para armazenar uma mensagem.
    # Verifica se a mensagem agendada está no futuro e se o remetente e destinario existe
    def post(self):
        data = Message.parser.parse_args()

        time_1 = data['message_dt']
        time_2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

        if time_1 < time_2:
            return {"message": "Horario deverá ser após o horario atual"}, 400
        elif EmployeeModel.find_employee_worker_id(data['sender_worker_id']) == None:
            return {"message": "Usuario de origem não existe"}, 400
        elif EmployeeModel.find_employee_worker_id(data['receiver_worker_id']) == None:
            return {"message": "Usuario de destino não existe"}, 400
        
        msg = MessageModel(**data)
        msg.save_message()

        return {"message": "Mensagem criada com sucesso"}, 201
        
class MessageItem(Resource):

    # Metodo GET para mensagens
    # A partir do ID de usuario e uma query retornada pelo MessageModel,
    # transforma todas as mensagens agendadas no banco de dados
    # e retorna como resposta
    def get(self, _id):
        result = MessageModel.find_messages(_id)

        msgs = []
        for row in result:
            msgs.append({
                "dt": row[0].isoformat(),
                "message_id": row[1],
                "message_dt": row[2].isoformat(),
                "sender_worker_id": row[3],
                "receiver_worker_id": row[4],
                "email": row[5],
                "phone": row[6],
                "message_app": row[7],
                "message": row[8]
            })

        return {"msgs": msgs}
    
    # Metodo DELETE para mensagens
    # Exclui uma mensagem a partir de seu id passado como
    # parâmetro na URL /msg/<id>
    def delete(self, _id):
        MessageModel.delete_message(_id)

        return {"message": "Mensagem excluida com sucesso"}
