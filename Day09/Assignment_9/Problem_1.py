#1
'''''
Library Management System
1. **For Users (Library Members):**
   - View a list of available books with details such as title, author, and genre.
   - Search for books by title, author, or genre.
   - Borrow a book (API updates the book status to "borrowed").
   - Return a borrowed book (API updates the book status to "available").

2. **For Librarians:**
   - Add new books to the library using a menu option.
   - Update book details like title, author, or genre.
   - Remove books from the library.'''



from flask import Flask,request,jsonify
from pymongo import MongoClient
import json
app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb3"]  # Database name
mycol = db["library"]  #table name

#1.view the books
@app.route("/books",methods=["GET"])
def view_books(): # to view all the books
    books = list(mycol.find({},{"_id":0}))
    return jsonify(books)

#2.to add the books
@app.route("/add_books",methods=["POST"])
def add_books():
    data = request.json
    new={
        "title":data["title"],
        "author":data["author"],
        "genre":data["genre"],
        "status":"available"
    }
    mycol.insert_one(new)
    return "Book added"

#3.to seacrh the books by title,genre,author
@app.route("/books/search",methods=["GET"])
def search_books():
    title=request.args.get("title") # get request for title and add in the variable title
    author=request.args.get("author")
    genre=request.args.get("genre")
    s={}
    if title:
        s["title"]=title #matching the title
    if author:
        s["author"]=author
    if genre:
        s["genre"]=genre

    books=list(mycol.find(s,{"_id":0}))
    if books:
        return jsonify(books)
    return jsonify({"no books found"})

# 4.to borrow the available books
@app.route("/books/borrow",methods=["PUT"])
def borrow_books():
    data = request.json
    title=data.get("title")
    book = mycol.find_one({"title":title,"status":"available"})
    if book:
        mycol.update_one({"title":title},{"$set":{"status":"borrowed"}})
        return jsonify({"message":f"you have borrowed '{title}'"})
    return jsonify({"no books found"})

#5.to return the books
@app.route("/books/return",methods=["PUT"])
def return_books():
    data = request.json
    title = data.get("title")
    book = mycol.find_one({"title":title,"status":"borrowed"})
    if book:
        mycol.update_one({"title":title},{"$set":{"status":"available"}})
        return jsonify({"book returned":title})
    return jsonify({title:"its not borrowed"})

#6.delete the books
@app.route("/book/remove",methods=["DELETE"])
def remove_books():
    title = request.args.get("title")
    book=mycol.find_one({"title":title})
    if book:
        mycol.delete_one({"title":title})
        return jsonify({"book removed":title})
    return jsonify({"no books found"})


if __name__ == '__main__':
    app.run(debug=True)











