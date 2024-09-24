from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import get_engine, Author, Book

def seed_database(session):
    # Create some authors
    author1 = Author(name='J.K. Rowling')
    author2 = Author(name='J.R.R. Tolkien')
    author3 = Author(name='George R.R. Martin')

    session.add_all([author1, author2, author3])
    session.commit()

    # Create some books
    book1 = Book(title='Harry Potter and the Philosopher\'s Stone')
    book2 = Book(title='The Hobbit')
    book3 = Book(title='A Game of Thrones')

    book1.authors.append(author1)
    book2.authors.append(author2)
    book3.authors.append(author3)

    session.add_all([book1, book2, book3])
    session.commit()

if __name__ == '__main__':
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    seed_database(session)
    print("Database seeded successfully!")
