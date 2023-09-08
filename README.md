# ZZ-Task

# Library Management System (Flask API)

<!-- This is a Flask API for a simple Library Management System. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations on a collection of books stored in a SQLite database. This README will guide you through the setup and usage of the API.

Prerequisites
Before running the application, ensure you have the following installed:

Python 3.x
Flask
Flask-JWT-Extended
Flask-SQLAlchemy
Flask-Migrate
Flask-Marshmallow
Marshmallow-SQLAlchemy
You can install these dependencies using pip:


pip install flask flask-jwt-extended flask-sqlalchemy flask-migrate flask-marshmallow marshmallow-sqlalchemy

Setup
Clone this repository to your local machine:

git clone https://github.com/islamkamran/ZZ-Task.git

Change to the project directory:
cd ZZ-Task

Create a virtual environment (recommended):
python -m venv venv

Activate the virtual environment:
source venv/bin/activate

Install the project dependencies:
pip install -r requirements.txt

Initialize the SQLite database:
flask db init
flask db migrate
flask db upgrade

Run the application:
python app.py -->

<!-- The API should now be running at http://localhost:5000.

API Endpoints

1. Create a New Book
Endpoint: /api/books
Method: POST
Description: Adds a new book to the library.
Parameters:
name (string, required): The name of the book.
company (string, required): The publishing company of the book.

2. Read All Books
Endpoint: /api/books-get
Method: GET
Description: Retrieves a list of all books in the library.

3. Read One Book by ID
Endpoint: /api/books/<int:id>/get-one
Method: GET
Description: Retrieves details of a single book by its ID.

4. Update One Book by ID (using PUT)
Endpoint: /api/books/<int:id>/update
Method: PUT
Description: Updates the details of a book by its ID.
Parameters:
name (string, optional): The new name of the book.
company (string, optional): The new publishing company of the book.

5. Update One Book by ID (using PATCH)
Endpoint: /api/books/<int:id>/update-patch
Method: PATCH
Description: Partially updates the details of a book by its ID.
Parameters:
name (string, optional): The new name of the book.
company (string, optional): The new publishing company of the book.

6. Delete One Book by ID
Endpoint: /api/books/<int:id>/delete
Method: DELETE
Description: Deletes a book from the library by its ID.

7. Delete All Books
Endpoint: /api/books/delete
Method: DELETE
Description: Deletes all books from the library. -->

<!-- Authentication -->
<!-- This API uses JWT (JSON Web Tokens) for authentication. To access protected endpoints, you need to obtain a valid access token. You can generate a token by sending a POST request to /api/auth/login with valid credentials. The token should be included in the Authorization header of your requests to protected endpoints with the prefix Bearer. -->
