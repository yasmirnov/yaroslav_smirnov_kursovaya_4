from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import auth_service, user_service
from project.setup.api.models import auth, auth_result


api = Namespace('auth')


@api.route('/register/') # регистрация, создание пользователя в БД
class AuthView(Resource):
    @api.expect(auth) # ожидаем получить модель auth (json c полями email, password)
    @api.response(201, description='OK') # в случае успешного выполнения возвращаем
    def post(self):
        user_service.create(request.json)
        return 'OK', 201


@api.route('/login/') # вход пользователя
class AuthView(Resource):
    @api.expect(auth)
    @api.marshal_with(auth_result, code=200)
    def post(self):
        """
        Аутентификация пользователя
        """
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)

        if None in [email, password]:
            abort(400)

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 200

    def put(self):
        """
        Создание новой пары токенов
        """
        data = request.json

        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)

        return tokens, 200
