'''Requirements:
- Build a RESTful API to manage all operations (CRUD for books, borrowing, and returning).
- Authenticate library members and librarians through an API.
- The command-line interface (CLI) should present menu options to navigate:
  - Example:
    ```
    1. View Available Books
    2. Search for a Book
    3. Borrow a Book
    4. Return a Book
    5. Exit '''

import requests
Api_url = "http://127.0.0.1:5000"

def display_menu():
   print("""
   Library Management System
   1. Add book
   2. View all books
   3. Delete book by id
   4. Search book by title
   5. Borrow Book by id
   6. Return book by id""")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    status = "available"
    response = requests.post(f"{Api_url}/add_book", json={"title": title, "author": author, "status": status})
    print(response.json())

def view_books():
    response = requests.get(f"{Api_url}/get_books")
    books = response.json()
    for book in books:
        print(book)

def delete_book():
    book_id = input("Enter book ID to delete: ")
    response = requests.delete(f"{Api_url}/delete_book/{book_id}")
    print(response.json())

def search_book_by_title():
    title = input("Enter book title to search: ")
    response = requests.get(f"{Api_url}/book/title/{title}")
    print(response.json())

def borrow_book():
    book_id = input("Enter book ID to borrow: ")
    response = requests.put(f"{Api_url}/book/borrow/{book_id}")
    print(response.json())

def return_book():
    book_id = input("Enter book ID to return: ")
    response = requests.put(f"{Api_url}/book/return/{book_id}")
    print(response.json())

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_book_by_title()
        elif choice == "5":
            borrow_book()
        elif choice == "6":
            return_book()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()