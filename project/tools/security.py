import base64
import hashlib
import hmac

import jwt
from flask import current_app, request, abort

from project.config import SECRET, ALGO


def generate_password_digest(password: str):
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(generate_password_digest(password)).decode('utf-8')


def compare_password(password_hash, other_password) -> bool:
    return hmac.compare_digest(
        base64.b64decode(password_hash),
        hashlib.pbkdf2_hmac('sha256',
                            other_password.encode('utf-8'),
                            salt=current_app.config['PWD_HASH_SALT'],
                            iterations=current_app.config['PWD_HASH_ITERATIONS'])
    )


def get_email_from_token(data):
    token = data['Authorization'].split('Bearer')[-1]
    data = jwt.decode(token, SECRET, algorithms=[ALGO])
    email = data['email']
    return email


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]

        try:
            user = jwt.decode(token, SECRET, algorithms=[ALGO])
            role = user.get("role")
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        if role != "admin":
            abort(403)
        return func(*args, **kwargs)
    return wrapper
