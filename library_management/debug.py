from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import get_engine, Author, Book, Borrower

def debug_queries():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example query to list all books with authors
    books = session.query(Book).all()
    for book in books:
        authors = ', '.join(author.name for author in book.authors)
        print(f'Book ID: {book.id} | Title: {book.title} | Authors: {authors}')

if __name__ == '__main__':
    debug_queries()
