from flask import Flask, jsonify, render_template

from project.exceptions import BaseServiceError
from project.setup.api import api
from project.setup.db import db
from project.views.auth import auth_ns, user_ns
from project.views.main.directors import director_ns
from project.views.main.genres import genre_ns
from project.views.main.movies import movie_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify(
        {'error': exception.message}
    ), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    # return app

    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(user_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(auth_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app
