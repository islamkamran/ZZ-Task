from flask import Flask,request,jsonify
from flask_jwt_extended import JWTManager, create_access_token
# import jwt # this is usually used when we want to decode the JWT token later on for authentication
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['JWT_SECRET_KEY'] = 'your-secret-key'

from models import db, Books

# Initialize Extensions
db.init_app(app)

# CODE BEFORE FLASK MIGRATIONS
# with app.app_context():
#     db.create_all()

ma = Marshmallow(app)
migrate = Migrate(app, db)


jwt_manager = JWTManager(app)

# Serialization/ De-Serialization Schema
class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Books

book_schema = BookSchema()
books_schema = BookSchema(many=True)


# ************************************************
#Library Management System CURD Operations
# ************************************************

# CREATE A NEW BOOK
#********************* 
@app.post('/api/books')
def create_book():
    name = request.form['name']
    company = request.form['company']
    if Books.query.filter_by(name = name).first():
        return jsonify({"message":"book already in store"}), 200
        
    new_book = Books(name = name, company = company)
    try:
        db.session.add(new_book)
        db.session.commit()

        return book_schema.jsonify(new_book)
    
    # CODE BEFORE MARSHMALLOW
        # token_payload = {
        #     "id": new_book.id,
        #     "name": new_book.name,
        #     "company": new_book.company
        # }
        # access_token = create_access_token(identity = token_payload)

        
    except Exception as e:
        db.session.rollback()
        return jsonify({"An error occuring while adding": str(e)})



# READ ALL BOOKS FROM DB
# **********************
@app.get('/api/books-get')
def get_all_books():
    try:
        books = Books.query.all()
        return books_schema.jsonify(books)
    
    # WITHOUT MARSHMALLOW COMMENTED CODE
        # books_list = []
        # for book in books:
        #     books_list.append({
        #         'book_id': book.id,
        #         'book_name': book.name,
        #         'book_company': book.company
        #     })
        # return jsonify({'message':'Books Returned Successfully', 'Books':books_list}), 200
    except Exception as e:
        return jsonify({"An error occuring while getting": str(e)})


# READ ONE BOOK UPON ID FROM DB
# *****************************
@app.get('/api/books/<int:id>/get-one')
def get_one_books(id):
    try:
        book = Books.query.filter_by(id = id).first()
        return book_schema.jsonify(book)
    
    # WITHOUT MARSHMALLOW COMMENTED CODE
        # one_book = {
        #     'book_id': book.id,
        #     'book_name': book.name,
        #     'book_company': book.company
        # }
        # return jsonify({'message':'Books Returned Successfully', 'book':one_book}), 200
    except Exception as e:
        return jsonify({"An error occuring while getting": str(e)})


# UPDATE BOOK UPON ID - USING PUT
# *******************************
@app.put('/api/books/<int:id>/update')
def update_one_books(id):
    try:
        if not Books.query.get(id):
            return "Book not Found", 404
        try:
            book = Books.query.get(id)
            name = request.form['name']
            company = request.form['company']
            if name is not None and company is not None:
                book.name = name
                book.company = company
                db.session.commit()
        except Exception as e:
            return "An error occuring while updating" + str(e)
        
        return book_schema.jsonify(book)
    
    # WITHOUT MARSHMALLOW COMMENTED CODE
        # updated_book = {
        #     'book_id': book.id,
        #     'book_name': book.name,
        #     'book_company': book.company
        # }        
        # return jsonify({'message':'Books Updated Successfully', 'book':updated_book}), 200
    except Exception as e:
        return jsonify({"An error occuring while updating": str(e)})
    


# UPDATE BOOK UPON ID - USING PATCH
# *********************************
@app.patch('/api/books/<int:id>/update-patch')
def update_one_books_part(id):
    try:
        if not Books.query.get(id):
            return "Book not Found", 404
        try:
            book = Books.query.get(id)
            if 'name' in request.form:
                book.name = request.form['name']
                db.session.commit()
            if 'company' in request.form:
                book.company = request.form['company']
                db.session.commit()

        except Exception as e:
            return jsonify({"message":"An error occuring while updating" + str(e)}), 200
        
        return book_schema.jsonify(book)
    
    # WITHOUT MARSHMALLOW COMMENTED CODE
        # updated_book = {
        #     'book_id': book.id,
        #     'book_name': book.name,
        #     'book_company': book.company
        # }        
        # return jsonify({'message':'Books Updated Successfully', 'book':updated_book}), 200
    except Exception as e:
        return jsonify({"An error occuring while Updating": str(e)})


# DELETE ONE BOOK FROM DB BY ID
# ******************************
@app.delete('/api/books/<int:id>/delete')
def delete_one_books(id):
    try:
        book = Books.query.get(id)
        if not book:
            return jsonify({"message":"Book not found"}), 404
        
        db.session.delete(book)
        db.session.commit()

        # Just to show which book is deleted
        return book_schema.jsonify(book)
    except Exception as e:
        return jsonify({"An error occuring while adding": str(e)})
       

# DELETE ALL BOOKS FROM DB
# ************************
@app.delete('/api/books/delete')
def delete_all_books():
    try:
        db.session.query(Books).delete()
        db.session.commit()

        return '', 204
    except Exception as e:
        return jsonify({"An error occuring while adding": str(e)})


if __name__ == '__main__':
   app.run(debug=True)
