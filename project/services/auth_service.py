import calendar
import datetime

import jwt
from flask import abort

from project.config import ALGO, SECRET
from project.services.users_service import UsersService
from project.tools.security import compare_password


class AuthService:
    def __init__(self, user_service: UsersService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            abort(404)

        if not is_refresh:
            if not compare_password(user.password, password):
                abort(400)

        data = {
            'email': user.email,
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SECRET,
                                  algorithm=ALGO)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SECRET,
                                   algorithm=ALGO)

        return {'access_token': access_token, 'refresh_token': refresh_token}

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(refresh_token,
                          SECRET,
                          algorithms=[ALGO])
        if 'email' not in data:
            abort(400)
        email = data.get('email')
        return self.generate_tokens(email, None, is_refresh=True)
