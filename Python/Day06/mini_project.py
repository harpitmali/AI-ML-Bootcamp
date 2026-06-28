def add_book(books):
    book_name = input("Enter book name: ")
    books.append(book_name)
    print("Book added successfully.")  

def remove_book(books):
    book_name = input("Enter book name: ")
    if book_name in books:
        books.remove(book_name)
        print("Book removed.")
    else:
        print("Book not found.")

def search_book(books):
    book_name = input("Enter book name: ")
    if book_name in books:
        print("Book available.")
    else:
        print("Book not available")

def display_books(books):
    if len(books) == 0:
        print("No books available.")
    else:
        i = 1
        for book in books:
            print(f"{i}. {book}")
            i += 1

books = []

while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Exit")

    option = int(input("Choose: "))

    if option == 1:
        add_book(books)
    elif option == 2:
        remove_book(books)
    elif option == 3:
        search_book(books)
    elif option == 4:
        display_books(books)
    elif option == 5:
        print("Thank You!")
        break
    else:
        print("Invalid choice")
        print("Choose between 1-5")
        print("Try again!")