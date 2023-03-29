from flask_restx import Namespace, Resource

from project.container import genre_service
from project.setup.api.models import genre
from project.setup.api.parsers import page_parser


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @genre_ns.expect(page_parser)
    @genre_ns.marshal_with(genre, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all genres.
        """
        return genre_service.get_all(**page_parser.parse_args())


@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    @genre_ns.response(404, 'Not Found')
    @genre_ns.marshal_with(genre, code=200, description='OK')
    def get(self, genre_id: int):
        """
        Get genre by id.
        """
        return genre_service.get_item(genre_id)
