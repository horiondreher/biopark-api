from flask_restful import Resource, reqparse

class EmployeeRegister(Resource):

    # parser para validação de dados enviados pelo client
    parser = reqparse.RequestParser()

    # Nome completo, usuário e senha não podem ser deixados em branco
    parser.add_argument(
        'fullname',
        type = str,
        required = True,
        help = "Este campo não pode ser deixado em branco"
    )
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = "Este campo não pode ser deixado em branco"
    )
    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = "Este campo não pode ser deixado em branco"
    )
    
    def post(self):
        data = EmployeeRegister.parser.parse_args()
        print(data)

        return 200


