# Simple Library Management System

library = []  # list to store books

def add_book():
    book = input("Enter book name: ")
    library.append(book)
    print(f"'{book}' added to the library.")

def display_books():
    if len(library) == 0:
        print("Library is empty.")
    else:
        print("Books in library:")
        for i, book in enumerate(library, 1):
            print(f"{i}. {book}")

def search_book():
    book = input("Enter book name to search: ")
    if book in library:
        print(f"'{book}' is available in the library.")
    else:
        print(f"'{book}' is not in the library.")

def delete_book():
    book = input("Enter book name to delete: ")
    if book in library:
        library.remove(book)
        print(f"'{book}' removed from the library.")
    else:
        print(f"'{book}' not found.")

# Main menu
while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("Exiting Library System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
