import logging

from project.config import DevelopmentConfig
from project.server import create_app

logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s')

app = create_app(DevelopmentConfig)


if __name__ == '__main__':
    app.run(port=25000)
