import logging

from project.config import config
from project.models import Genre
from project.server import create_app, db

logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s')

app = create_app(config)

if __name__ == 'main':
    app.run()
