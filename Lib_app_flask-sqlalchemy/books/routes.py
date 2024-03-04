from flask import (
    redirect,
    render_template, 
    request,
    url_for,
)

from app import db # Объект для работы с базой данных
from books import books_blueprint
from books.models import Book


def main_menu():
    return render_template(
        "home/home.html"
    )


@books_blueprint.route("/show_books") # Регистрируем роут в нашем модуле с указанными методами
def show_all_books():
    data = db.session.execute(db.select(Book).order_by(Book.id)).scalars().fetchall()
    return render_template(
            "show_books.html",
            data=data
        )

@books_blueprint.route("/add_book", methods=["GET", "POST"])
def add_book():

    if request.method == "GET":
        return render_template(
            "add_book.html"
        )
    elif request.method == "POST":
        name = request.form["name"]
        author_id = request.form["author_id"]
        book = Book(name=name, author_id=author_id)
        db.session.add(book)
        db.session.commit()
        return redirect(
            url_for("books.show_all_books")
        )

@books_blueprint.route("/update_book", methods=["GET", "POST"])
def update_book():
    if request.method == "GET":
        return render_template(
            "update_book.html"
        )
    elif request.method == "POST":
        book = request.form["book"]
        book_name = request.form["book_name"]
        books = db.session.query(Book).filter(Book.name.ilike(book)).all()
        if books:
            for book in books:
                book.name = book_name
            db.session.commit()
        return redirect(
                url_for("books.show_all_books")
            )
    
@books_blueprint.route("/delete_book", methods=["GET", "POST"])
def delete_book():
    if request.method == "GET":
        return render_template(
            "delete_book.html"
        )
    elif request.method == "POST":
        book = request.form["book"]
        book = db.session.query(Book).filter(Book.name == book).first()
        db.session.delete(book)
        db.session.commit()
        return redirect(
            url_for("books.show_all_books")
        )
    

@books_blueprint.route("/find_book", methods=["GET", "POST"])
def find_book():

    if request.method == "GET":
        return render_template(
            "find_book.html"
        )
    
    elif request.method == "POST":
        book_name = request.form["book_name"]
        f_book = db.session.query(Book).filter(Book.name.ilike(f"%{book_name}%")).all()
        return render_template(
            "solo_book.html",
            f_book=f_book,
        )