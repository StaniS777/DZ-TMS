from flask import (
    redirect,
    render_template, 
    request,
    url_for,
)

from app import db # Объект для работы с базой данных
from authors import authors_blueprint
from books.models import Author


def main_menu():
    return render_template(
        "home/home.html"
    )


@authors_blueprint.get("/show_authors")
def show_authors():
    data = db.session.execute(db.select(Author)).fetchall()
    if data:
        return render_template(
            "show_authors.html",
            data=data
        )

@authors_blueprint.route("/add_author", methods=["GET", "POST"])
def add_author():
    if request.method == "GET":
        return render_template(
            "add_author.html"
        )
    elif request.method == "POST":
        author_name = request.form["author_name"]
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        return redirect(
            url_for("authors.show_authors")
        )
    
@authors_blueprint.route("/delete_author", methods=["GET", "POST"])

def delete_author():
    if request.method == "GET":
        return render_template(
            "delete_author.html"
        )
        
    elif request.method == "POST":
        author = request.form["author"]
        author = db.session.query(Author).filter(Author.name == author).first()      
        db.session.delete(author)
        db.session.commit()
        return redirect(
            url_for("authors.show_authors")
        )
