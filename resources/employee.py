from flask_restful import Resource, reqparse
from models.employee import EmployeeModel

class EmployeeRegister(Resource):

    # parser para validação de dados enviados pelo client
    parser = reqparse.RequestParser()

    # Nome completo, usuário e senha não podem ser deixados em branco.
    # O parser disponibilizado pelo flask será responsável por autenticar
    # o documento json enviado na requisição e retornará uma resposta 400 - bad request
    # se os parâmetros não forem cumpridos
    parser.add_argument('worker_id', type = int, required = True, help = "ID do funcionário é necessário")
    parser.add_argument('fullname', type = str, required = True, help = "Nome completo é necessário")
    parser.add_argument('username', type = str, required = True, help = "Usuário é necessário")
    parser.add_argument('password', type = str, required = True, help = "Senha é necessária")
    
    # Método POST de criação de usuário.
    # Realiza a verificação dos dados com o parse e também verifica se o usuário já existe
    def post(self):
        data = EmployeeRegister.parser.parse_args()

        if EmployeeModel.find_employee_worker_id(data['worker_id']):
            return {"message": "Este número de ID já existe"}, 400 # retorna 400 - BAD REQUEST se usuário já existe
        elif EmployeeModel.find_employee_username(data['username']):
            return {"message": "Este nome de usuario já existe"}, 400 # retorna 400 - BAD REQUEST se usuário já existe

        employee = EmployeeModel(**data)
        employee.save_employee()
        
        return {"message": "Usuário criado com sucesso"}, 201 # retorna 201 - CREATED para criação 


