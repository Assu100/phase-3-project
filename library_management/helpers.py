from sqlalchemy.orm import Session
from models import Author, Book

def get_author_by_id(session: Session, author_id: int) -> Author:
    """Fetch an author by ID."""
    return session.query(Author).get(author_id)

def get_book_by_id(session: Session, book_id: int) -> Book:
    """Fetch a book by ID."""
    return session.query(Book).get(book_id)

def get_all_books(session: Session):
    """Fetch all books."""
    return session.query(Book).all()

def get_all_authors(session: Session):
    """Fetch all authors."""
    return session.query(Author).all()
