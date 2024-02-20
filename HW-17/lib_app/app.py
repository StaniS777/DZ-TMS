from flask import Flask
from flask import (
    request, 
    render_template, 
    redirect,
    url_for
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from books import books, Book
from db import DBrepository


app = Flask(__name__)
engine = create_engine("postgresql://postgres:Qawsedr5@localhost:5432/stanis")
Session = sessionmaker(bind=engine)
session = Session()
repo = DBrepository(session=session)


@app.get("/")
def home():
    return render_template(
        "start.html",
    )


@app.get("/menu")
def menu():
    return render_template(
        "menu.html"
    )

@app.get("/menu/show_books")
def show_books():
    data = repo.show_all_books()
    if data:
        return render_template(
            "show_books.html",
            data=data
        )

@app.get("/menu/show_authors")
def show_authors():
    data = repo.show_authors()
    if data:
        return render_template(
            "show_authors.html",
            data=data
        )
    
@app.route("/menu/add_book", methods=["GET", "POST"])
def add_book():

    if request.method == "GET":
        return render_template(
            "add_book.html"
        )
    elif request.method == "POST":
        name = request.form["name"]
        author_id = request.form["author_id"]
        repo.add_book(name, author_id)
        return redirect(
            url_for("show_books")
        )
    
@app.route("/menu/update_book", methods=["GET", "POST"])
def update_book():
    if request.method == "GET":
        return render_template(
            "update_book.html"
        )
    elif request.method == "POST":
        book = request.form["book"]
        book_name = request.form["book_name"]
        repo.update_book(book, book_name)
        return redirect(
            url_for("show_books")
        )
    
@app.route("/menu/delete_book", methods=["GET", "POST"])
def delete_book():
    if request.method == "GET":
        return render_template(
            "delete_book.html"
        )
    elif request.method == "POST":
        book = request.form["book"]
        repo.delete_book(book)
        return redirect(
            url_for("show_books")
        )

@app.route("/menu/add_author", methods=["GET", "POST"])
def add_author():

    if request.method == "GET":
        return render_template(
            "add_author.html"
        )
    elif request.method == "POST":
        author_name = request.form["author_name"]
        repo.add_author(author_name)
        return redirect(
            url_for("show_authors")
        )
    
@app.route("/menu/find_book", methods=["GET", "POST"])
def find_book():

    if request.method == "GET":
        return render_template(
            "find_book.html"
        )
    
    elif request.method == "POST":
        book_name = request.form["book_name"]
        books = repo.find_book(book_name)
        return render_template(
            "solo_book.html",
            books=books,
        )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000")


