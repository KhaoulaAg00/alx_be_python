# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # Testing Book class initialization
    book1 = Book("Pride and Prejudice", "Jane Austen")
    print(f"Book 1: {book1.title} by {book1.author}")

    # Testing EBook class initialization
    ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)
    print(f"EBook 1: {ebook1.title} by {ebook1.author}, File Size: {ebook1.file_size}KB")

    # Testing PrintBook class initialization
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    print(f"PrintBook 1: {printbook1.title} by {printbook1.author}, Page Count: {printbook1.page_count}")

    # Testing Library class and methods
    my_library = Library()

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(ebook1)
    my_library.add_book(printbook1)

    # List all books in the library
    print("\nListing all books in the library:")
    my_library.list_books()

if __name__ == "__main__":
    main()
