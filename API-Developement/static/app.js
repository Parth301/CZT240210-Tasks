const apiUrl = "http://127.0.0.1:5000/books";

async function fetchBooks() {
    const response = await fetch(apiUrl);
    const books = await response.json();
    const bookList = document.getElementById("book-list");
    bookList.innerHTML = "";
    books.forEach(book => {
        const li = document.createElement("li");
        li.textContent = `${book.title} by ${book.author} (${book.year})`;
        li.innerHTML += ` <button onclick="deleteBook(${book.id})">Delete</button>`;
        bookList.appendChild(li);
    });
}

async function addBook() {
    const title = document.getElementById("title").value;
    const author = document.getElementById("author").value;
    const year = parseInt(document.getElementById("year").value);
    const response = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, author, year })
    });
    if (response.ok) fetchBooks();
}
 async function updateBook() {
    const bookId = document.getElementById("update-id").value;
    const title = document.getElementById("update-title").value;
    const author = document.getElementById("update-author").value;
    const year = document.getElementById("update-year").value;

    const updatedBook = {};
    if (title) updatedBook.title = title;
    if (author) updatedBook.author = author;
    if (year) updatedBook.year = parseInt(year);

    fetch(`/books/${bookId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedBook)
    })
    .then(response => response.json())
    .then(() => {
        fetchBooks(); // Refresh the list of books
    });
}

async function deleteBook(id) {
    await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
    fetchBooks();
}

fetchBooks();
