from utils import books, issue_books

def return_book():
    book_name = input("Enter book name to be returned: ").upper()
    if book_name in issue_books:
        issue_books.remove(book_name)
        books.append(book_name)
        print("Book returned")
    else:
        print("blablabla!!!") 