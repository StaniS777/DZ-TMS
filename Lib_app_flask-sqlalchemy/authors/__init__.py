from flask import Blueprint


authors_blueprint = Blueprint(
    "authors",
    __name__,
    template_folder="templates",
)


from authors.routes import *
