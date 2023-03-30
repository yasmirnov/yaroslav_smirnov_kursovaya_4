from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(120), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'Movies'

    title = Column(String(240), nullable=False)
    description = Column(String(400), nullable=False)
    trailer = Column(String(120), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)

    genre_id = Column(Integer, ForeignKey(Genre.id), nullable=False)
    genre = relationship('Genre')
    director_id = Column(Integer, ForeignKey(Director.id), nullable=False)
    director = relationship('Director')


class User(models.Base):
    __tablename__ = 'Users'

    email = Column(String(240), unique=True, nullable=False)
    password = Column(String(240), nullable=False)
    name = Column(String(160))
    surname = Column(String(160))

    # favourite_genre = Column(Integer, ForeignKey(Genre.id))
    # genre = relationship('Genre')
