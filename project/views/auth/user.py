from flask import request, abort
from flask_restx import Namespace, Resource

from project.container import user_service
from project.setup.api.models import user
from project.tools.security import admin_required

user_ns = Namespace('users')


@user_ns.route("/")
class UsersView(Resource):
    @admin_required
    @user_ns.response(200, "OK")
    @user_ns.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        return user_service.get_all()


@user_ns.route("/<int:user_id>")
class UserView(Resource):
    @admin_required
    @user_ns.response(200, "OK")
    @user_ns.response(404, 'Not Found')
    @user_ns.response(500, 'Unexpected error')
    @user_ns.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self, user_id: int):
        return user_service.get_one(user_id)

    def patch(self, uid: int):
        req_json = request.json
        if not req_json:
            abort(400)
        if not req_json.get("id"):
            req_json['id'] = uid

        return user_service.update(req_json)


@user_ns.route("/password/<int:user_id>")
class UserPatchView(Resource):
    @admin_required
    @user_ns.response(200, "OK")
    @user_ns.response(404, 'Not Found')
    def put(self, uid: int):
        req_json = request.json
        password_1 = req_json.get("password_1", None)
        password_2 = req_json.get("password_2", None)
        if None in [password_1, password_2]:
            abort(400)
        if not password_1 or not password_2:
            abort(400)
        if not req_json.get("id"):
            req_json['id'] = uid

        return user_service.update_password(req_json)
