from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"id": 4, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 5, "title": "Moby-Dick", "author": "Herman Melville", "year": 1851},
    {"id": 6, "title": "War and Peace", "author": "Leo Tolstoy", "year": 1869},
    {"id": 7, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866},
    {"id": 8, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    {"id": 9, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 10, "title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953},
    {"id": 11, "title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
    {"id": 12, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"id": 13, "title": "Jane Eyre", "author": "Charlotte Brontë", "year": 1847},
    {"id": 14, "title": "Wuthering Heights", "author": "Emily Brontë", "year": 1847},
    {"id": 15, "title": "The Odyssey", "author": "Homer", "year": -800},
    {"id": 16, "title": "The Iliad", "author": "Homer", "year": -750},
    {"id": 17, "title": "Great Expectations", "author": "Charles Dickens", "year": 1861},
    {"id": 18, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "year": 1880},
    {"id": 19, "title": "Anna Karenina", "author": "Leo Tolstoy", "year": 1877},
    {"id": 20, "title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "year": 1967},
    {"id": 21, "title": "The Divine Comedy", "author": "Dante Alighieri", "year": 1320},
    {"id": 22, "title": "Dracula", "author": "Bram Stoker", "year": 1897},
    {"id": 23, "title": "Frankenstein", "author": "Mary Shelley", "year": 1818},
    {"id": 24, "title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "year": 1890},
    {"id": 25, "title": "Ulysses", "author": "James Joyce", "year": 1922},
    {"id": 26, "title": "The Metamorphosis", "author": "Franz Kafka", "year": 1915},
    {"id": 27, "title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "year": 1865},
]
@app.route("/")
def home():
    return render_template("index.html", books=books)

@app.route("/add", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")
    new_id = books[-1]["id"] + 1 if books else 1
    books.append({"id": new_id, "title": title, "author": author, "year": int(year)})
    return redirect(url_for("home"))

@app.route("/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
