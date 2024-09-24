from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

book_author_association = Table(
    'book_author', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', secondary=book_author_association, back_populates='authors')

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    authors = relationship('Author', secondary=book_author_association, back_populates='books')
    borrowers = relationship('Borrower', back_populates='book')

class Borrower(Base):
    __tablename__ = 'borrowers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship('Book', back_populates='borrowers')

def get_engine(db_url='sqlite:///library.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()