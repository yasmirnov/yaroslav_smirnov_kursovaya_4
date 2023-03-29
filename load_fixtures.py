from contextlib import suppress
from typing import Any, Dict, List, Type

from sqlalchemy.exc import IntegrityError

from project.config import DevelopmentConfig
from project.models import Genre, Movie, Director
from project.server import create_app
from project.setup.db import db, models
from project.utils import read_json


def load_data(data: List[Dict[str, Any]], model: Type[models.Base]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


# if __name__ == '__main__':
#     fixtures: Dict[str, List[Dict[str, Any]]] = read_json("fixtures.json")

    app = create_app(DevelopmentConfig)

    data = read_json("fixtures.json")

    with app.app_context():
        for genre in data["genres"]:
            db.session.add(Genre(id=genre["pk"], name=genre["name"]))
        for director in data["directors"]:
            db.session.add(Director(id=director["pk"], name=director["name"]))
        for movie in data["movies"]:
            db.session.add(
                Movie(id=movie["pk"], title=movie["title"], description=movie["description"], trailer=movie["trailer"],
                      year=movie["year"], rating=movie["rating"], genre_id=movie["genre_id"],
                      director_id=movie["director_id"]))

        try:
            db.session.commit()
        except IntegrityError:
            print("Fixtures already loaded")


    # with app.app_context():
    #     load_data(fixtures['genres'], Genre)
    #
    #     with suppress(IntegrityError):
    #         db.session.commit()
