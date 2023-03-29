from flask import request
from flask_restx import Namespace, Resource

from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser, status_page_parser


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MovieView(Resource):
    @movie_ns.expect(status_page_parser)
    # проверка данных (тот ли формат данных), которые мы получили на выходе из return
    @movie_ns.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        status = request.args.get('status')
        return movie_service.get_all(status=status, **page_parser.parse_args())


@movie_ns.route('/<int:movie_id>/')
class MovieView(Resource):
    # обработка ошибок
    @movie_ns.response(404, 'Not Found')
    @movie_ns.response(500, 'Unexpected error')
    # проверка данных (тот ли формат данных), которые мы получили на выходе из return
    @movie_ns.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        return movie_service.get_item(movie_id)

