# phase-3-project
# phase-3-project
# Library Management CLI

A simple command-line interface (CLI) application for managing a library system. This application allows you to add authors, books, and borrowers, and perform various operations related to books and authors.

## Features

- Add new authors and books
- Borrow and return books
- Search for books by title
- List all books, authors, and borrowers
- Remove books from the library
- Seed the database with initial data

## Requirements

- Python 3.6 or higher
- SQLAlchemy
- Click
- SQLite 

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Assu 100/phase-3-project
   cd library-management

2. Install dependencies:
    ```bash
    pipenv install
    pipenv shell
    pip install SQLAlchemy

## Database Setup
1. Initialize the database:
    ```bash
    pipenv run python cli.py

2. Seed the database:
    ```bash
    python seed.py

## Usage
1. Add author:
    ```bash
    python cli.py add_author NAME

2. Add a book:
    ```bash
    python cli.py add_book TITLE AUTHOR_ID

3. Borrow a book:
    ```bash
    python cli.py borrow_book NAME BOOK_ID

4. Return a book:
    ```bash
    python cli.py return_book BOOK_ID

5. Search a book:
    ```bash
    python cli.py search_book TITLE

6. Remove a book:
    ```bash
    python cli.py remove_book BOOK_ID

7. List all books:
    ```bash
    python cli.py list_books

8. List all authors:
    ```bash
    python cli.py list_authors

9. List all borrowers:
    ```bash
    python cli.py list_borrowers

## Debugging
    ```bash
    python debug.py

## Migrations with alembic
1. Install alembic:
    ```bash
    pip install alembic

2. Initialize alembic:
    ```bash
    alembic init migrations

3. Configure alembic:
    sqlalchemy.url = sqlite:///library.db

4. Create a new migration:
    ```bash
    alembic revision --autogenerate -m "Initial migration"

5. Apply migrations:
    ```bash
    alembic upgrade head
