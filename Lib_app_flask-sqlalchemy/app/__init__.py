from flask import Flask

from app.config import Config


app = Flask(__name__)

app.config.from_object(Config) # Конфигурация приложения и его компонентов

from app.db import db

db.init_app(app) # Подключение базы данных к приложению


from books import books_blueprint
from authors import authors_blueprint

app.register_blueprint(
    books_blueprint,
    url_prefix="/books",
) 

app.register_blueprint(
    authors_blueprint,
    url_prefix="/authors",
) 

from app.routes import *
