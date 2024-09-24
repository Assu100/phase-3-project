import click
from helpers import get_author_by_id, get_book_by_id, get_all_books, get_all_authors
from models import get_engine, get_session, Author, Book, Borrower

engine = get_engine()
session = get_session(engine)

@click.group()
def cli():
    """Library Management CLI"""
    pass

@click.command()
@click.argument('name')
def add_author(name):
    """Add a new author."""
    author = Author(name=name)
    session.add(author)
    session.commit()
    click.echo(f'Added author: {name}')

@click.command()
@click.argument('title')
@click.argument('author_ids', type=int, nargs=-1)
def add_book(title, author_ids):
    """Add a new book with specified authors."""
    book = Book(title=title)
    for author_id in author_ids:
        author = session.query(Author).get(author_id)
        if author:
            book.authors.append(author)
        else:
            click.echo(f'Author ID {author_id} not found.')
    session.add(book)
    session.commit()
    click.echo(f'Added book: {title}')

@click.command()
@click.argument('name')
@click.argument('book_id', type=int)
def borrow_book(name, book_id):
    """Borrow a book."""
    book = session.query(Book).get(book_id)
    if book:
        borrower = Borrower(name=name, book=book)
        session.add(borrower)
        session.commit()
        click.echo(f'{name} borrowed "{book.title}"')
    else:
        click.echo('Book not found!')

@click.command()
@click.argument('book_id', type=int)
def return_book(book_id):
    """Return a borrowed book."""
    borrower = session.query(Borrower).filter(Borrower.book_id == book_id).first()
    if borrower:
        session.delete(borrower)
        session.commit()
        click.echo(f'Book ID {book_id} returned.')
    else:
        click.echo('No borrower found for this book.')

@click.command()
@click.argument('title')
def search_book(title):
    """Search for a book by title."""
    books = session.query(Book).filter(Book.title.ilike(f'%{title}%')).all()
    if books:
        for book in books:
            authors = ', '.join(author.name for author in book.authors)
            click.echo(f'Book ID: {book.id} | Title: {book.title} | Authors: {authors}')
    else:
        click.echo('No books found with that title.')

@click.command()
@click.argument('book_id', type=int)
def remove_book(book_id):
    """Remove a book from the library."""
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        click.echo(f'Removed book: {book.title}')
    else:
        click.echo('Book not found!')

@click.command()
def list_books():
    """List all books in the library."""
    books = session.query(Book).all()
    for book in books:
        authors = ', '.join(author.name for author in book.authors)
        click.echo(f'Book ID: {book.id} | Title: {book.title} | Authors: {authors}')

@click.command()
def list_authors():
    """List all authors."""
    authors = session.query(Author).all()
    for author in authors:
        click.echo(f'Author ID: {author.id} | Name: {author.name}')

@click.command()
def list_borrowers():
    """List all borrowers."""
    borrowers = session.query(Borrower).all()
    for borrower in borrowers:
        click.echo(f'Borrower ID: {borrower.id} | Name: {borrower.name} | Book: {borrower.book.title}')

# Add all commands to the CLI
cli.add_command(add_author)
cli.add_command(add_book)
cli.add_command(borrow_book)
cli.add_command(return_book)
cli.add_command(search_book)
cli.add_command(remove_book)
cli.add_command(list_books)
cli.add_command(list_authors)
cli.add_command(list_borrowers)

if __name__ == '__main__':
    cli()
