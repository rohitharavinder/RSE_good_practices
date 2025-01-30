# Bookstore Package

[![Tests](https://github.com/zbmed-semtec/RSE_good_practices/actions/workflows/test.yml/badge.svg)](https://github.com/zbmed-semtec/RSE_good_practices/actions/workflows/test.yml)
[![Lint](https://github.com/zbmed-semtec/RSE_good_practices/actions/workflows/lint.yml/badge.svg)](https://github.com/zbmed-semtec/RSE_good_practices/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/rohitharavinder/RSE_good_practices/branch/feature%2Fbook-ratings/graph/badge.svg?token=JJS8D0RHLW)](https://codecov.io/gh/rohitharavinder/RSE_good_practices)
[![PyPI version](https://badge.fury.io/py/zbmed-bookstore.svg)](https://badge.fury.io/py/zbmed-bookstore)
[![Google Slides](https://img.shields.io/badge/Presentation-Mini%20Hackathon-purple)](https://docs.google.com/presentation/d/1ezF3WL1kR0J2lEt98TTzusaUBnCQYRoiEwdxfzzmKTo/preview)  


A demonstration package for teaching Python best practices. This package implements a simple book management system to illustrate:

- Clean code principles
- Proper package structure
- Good naming conventions
- Comprehensive documentation
- Type hints
- Testing practices

## Project Structure

```
bookstore/
├── src/
│   └── bookstore/
│       ├── __init__.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── book.py
│       ├── repositories/
│       │   ├── __init__.py
│       │   └── book_repository.py
│       └── exceptions/
│           ├── __init__.py
│           └── book_exceptions.py
└── tests/
    └── test_book.py
```

## Installation

For development:
```bash
pip install -e ".[dev]"
```

## Usage Example

```python
from bookstore.models.book import Book
from bookstore.repositories.book_repository import BookRepository

# Create a new book
book = Book(
    isbn="978-0-7475-3269-9",
    title="Harry Potter and the Philosopher's Stone",
    author="J.K. Rowling",
    publication_year=1997
)

# Store the book
repository = BookRepository()
repository.add_book(book)

# Retrieve a book
found_book = repository.get_book_by_isbn("978-0-7475-3269-9")
```

## Development Practices Demonstrated

1. **Clear Module Structure**: Separation of concerns between models, repositories, and exceptions
2. **Type Hints**: All functions include proper type annotations
3. **Documentation**: Google-style docstrings with examples
4. **Error Handling**: Custom exceptions and proper error messages
5. **Testing**: Comprehensive unit tests with pytest
6. **Clean Code**: Short, focused methods with clear responsibilities

# Contributing

This is an educational project. Feel free to fork and experiment, but we have some tasks for you to complete.

## Tasks 1
Add Book Categories/Genres

Branch name: feature/book-categories

Scope:
- Add category field to Book class
- Add category validation
- Update repository to search by category

PR Learning Points:
- Single responsibility principle
- Database schema changes
- Test coverage for new field

## Tasks 2
Add Book Search Functionality

Branch name: feature/search-books

Scope:
- Add search by title/author
- Implement fuzzy matching
- Add search result pagination

PR Learning Points:
- Algorithm implementation
- Performance considerations
- Documentation of search parameters

## Tasks 3
Add Book rating

Branch name: feature/book-ratings

Scope:
- Add Rating class
- Implement rating statistics
- Add rating constraints (1-5 stars)

PR Learning Points:
- Relationship between models
- Data validation
- Statistical calculations

## Tasks 4
Add Book Import/Export

Branch name: feature/import-export

Scope:
- CSV import/export
- JSON serialization
- Data validation

PR Learning Points:
- File handling
- Data formats
- Error handling

## Branch handling
It is important to know how to hadle and operate with branches.

## Contributing
Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to contribute to this project.

### PR Template
Please refer to the [PR Template](.github/pull_request_template.md) on the expected format for PRs.

## Continuous Integration

This project uses GitHub Actions for continuous integration and deployment:

- **Testing**: Automated tests run on multiple Python versions (3.8-3.11)
- **Code Coverage**: Coverage reports are uploaded to Codecov
- **Linting**: Code quality checks using Black, isort, mypy, and pylint
- **Publishing**: Automatic package publishing to PyPI on new releases

### Status Checks

Before merging a PR, ensure all status checks pass:
1. All tests pass across Python versions
2. Code coverage meets minimum threshold (90%)
3. Code follows style guidelines (Black, isort)
4. No type checking errors (mypy)
5. No linting issues (pylint)
