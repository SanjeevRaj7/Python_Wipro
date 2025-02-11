'''Problem Statement 1: **Library Management System (Command-Line Based)**

Develop a command-line-based library management system where users can interact through menus. The system will use a RESTful API to manage library operations like searching for, borrowing, and returning books.

#### Key Features:
1. **For Users (Library Members):**
   - View a list of available books with details such as title, author, and genre.
   - Search for books by title, author, or genre.
   - Borrow a book (API updates the book status to "borrowed").
   - Return a borrowed book (API updates the book status to "available").

2. **For Librarians:**
   - Add new books to the library using a menu option.
   - Update book details like title, author, or genre.
   - Remove books from the library.'''



from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# Database
client = MongoClient("mongodb://localhost:27017/")
db = client['mydb3']  # Database name
mycol = db["library1"]  # Collection name


# 1.add books
@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.json

    # Insert user data into MongoDB
    book_data = {
        "title": data['title'],
        "author": data['author'],
        "status": data['status']
    }
    result = mycol.insert_one(book_data)
    book_id = result.inserted_id

    return jsonify({"message": "book added", "book_id": str(book_id)}), 201

# 2.view books
@app.route('/get_books', methods=['GET'])
def get_books():
    books = mycol.find() #get all the books
    book_list = [{"Book id": str(data["_id"]),"Book_title":data['title'],"Book_author":data['author'],"Book_status":data['status']} for data in books]

    return jsonify(book_list)


# 3.delete books
@app.route('/delete_book/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        book=mycol.find_one({"_id": ObjectId(book_id)})
        if not book:
            return jsonify({"message": "book not found"}), 404
        if book['status'] == "borrowed":
            return jsonify({"message": "can't delete a borrowed book"}), 400
        result=mycol.delete_one({"_id":ObjectId(book_id)})
        if result.deleted_count==0:
            return jsonify({"message":"book not found"}),404

        return jsonify({"message":"book deleted successfully"}), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 500

# 4.search by title
@app.route('/book/title/<book_title>', methods=['GET'])
def get_book_by_title(book_title):
    book_title=mycol.find_one({"title":book_title})
    result=[{"book_Title":book_title['title'],"book_author":book_title['author'],"book_status":book_title['status']}]
    return jsonify(result)

#5.borrow book
@app.route('/book/borrow/<book_id>', methods=['PUT'])
def borrow_book(book_id):
    try:
        book = mycol.find_one({"_id": ObjectId(book_id)})
        if not book:
            return jsonify({"message": "Book not found"}), 404
        if book["status"] == "borrowed":
            return jsonify({"message": "Book is already borrowed"}), 400

        result = mycol.update_one({"_id": ObjectId(book_id)}, {"$set": {"status": "borrowed"}})
        if result.modified_count == 1:
            return jsonify({"message": "Book borrowed successfully"}), 200
        else:
            return jsonify({"message": "Book cannot be borrowed"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# 6.return book
@app.route('/book/return/<book_id>', methods=['PUT'])
def return_book(book_id):
    try:
        book = mycol.find_one({"_id": ObjectId(book_id)})
        if not book:
            return jsonify({"message": "Book not found"}), 404
        if book["status"] == "available":
            return jsonify({"message": "Book is already available"}), 400

        result = mycol.update_one({"_id": ObjectId(book_id)}, {"$set": {"status": "available"}})
        if result.modified_count == 1:
            return jsonify({"message": "Book returned successfully"}), 200
        else:
            return jsonify({"message": "Book cannot be returned"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)