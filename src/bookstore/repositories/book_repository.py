"""Repository module for managing book storage and retrieval operations."""

from datetime import datetime
from typing import Dict, List, Optional, Protocol

from ..exceptions.book_exceptions import DuplicateBookError
from ..models.book import Book


class StorageBackend(Protocol):
    """
    Protocol defining the interface for storage backends.

    This demonstrates the use of dependency injection and interface segregation.
    Different storage implementations (e.g., in-memory, file-based, database)
    can be used as long as they implement this protocol.
    """

    def save(self, key: str, data: dict) -> None:
        """Save data with the given key."""
        ...

    def load(self, key: str) -> Optional[dict]:
        """Load data for the given key."""
        ...

    def delete(self, key: str) -> None:
        """Delete data for the given key."""
        ...


class InMemoryStorage:
    """
    A simple in-memory storage implementation.

    This class demonstrates a concrete implementation of the StorageBackend
    protocol, using a dictionary as the storage mechanism.
    """

    def __init__(self) -> None:
        self._storage: Dict[str, dict] = {}

    def save(self, key: str, data: dict) -> None:
        """Save data to in-memory storage."""
        self._storage[key] = data

    def load(self, key: str) -> Optional[dict]:
        """Load data from in-memory storage."""
        return self._storage.get(key)

    def delete(self, key: str) -> None:
        """Delete data from in-memory storage."""
        self._storage.pop(key, None)


class BookRepository:
    """
    Repository for managing book operations.

    This class demonstrates:
    - Dependency injection (storage backend)
    - Single Responsibility Principle
    - Interface segregation
    - Clean method naming
    - Proper error handling

    Example:
        >>> storage = InMemoryStorage()
        >>> repo = BookRepository(storage)
        >>> book = Book(
        ...     isbn="978-0-7475-3269-9",
        ...     title="Harry Potter",
        ...     author="J.K. Rowling",
        ...     publication_year=1997
        ... )
        >>> repo.add_book(book)
        >>> found_book = repo.get_book_by_isbn(book.isbn)
        >>> found_book.title == "Harry Potter"
        True
    """

    def __init__(self, storage: Optional[StorageBackend] = None) -> None:
        """
        Initialize the repository with a storage backend.

        Args:
            storage: Implementation of StorageBackend protocol
                    If None, uses InMemoryStorage
        """
        self._storage = storage or InMemoryStorage()

    def add_book(self, book: Book) -> None:
        """
        Add a book to the repository.

        Args:
            book: The book to add

        Raises:
            DuplicateBookError: If a book with the same ISBN already exists
        """
        if self.get_book_by_isbn(book.isbn) is not None:
            raise DuplicateBookError(book.isbn)

        self._storage.save(book.isbn, self._book_to_dict(book))

    def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
        """
        Retrieve a book by its ISBN.

        Args:
            isbn: The ISBN to look up

        Returns:
            The book if found, None otherwise
        """
        data = self._storage.load(isbn)
        return self._dict_to_book(data) if data else None

    def delete_book(self, isbn: str) -> None:
        """
        Delete a book from the repository.

        Args:
            isbn: The ISBN of the book to delete
        """
        self._storage.delete(isbn)

    @staticmethod
    def _book_to_dict(book: Book) -> dict:
        """Convert a Book object to a dictionary."""
        return {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "publication_year": book.publication_year,
            "description": book.description,
            "added_at": book.added_at.isoformat(),
        }

    @staticmethod
    def _dict_to_book(data: dict) -> Book:
        """Convert a dictionary to a Book object."""
        return Book(
            isbn=data["isbn"],
            title=data["title"],
            author=data["author"],
            publication_year=data["publication_year"],
            description=data["description"],
            added_at=datetime.fromisoformat(data["added_at"]),
        )


class RatingRepository:
    """
    Repository for managing book ratings.
    """
    def __init__(self, storage: Optional[StorageBackend] = None) -> None:
        """
        Initialize the repository with a rating storage backend.

        Args:
            storage: Implementation of StorageBackend protocol
                    If None, uses InMemoryStorage
        """
        self._ratings = InMemoryStorage()
        self._ratings = self._ratings._storage
    
    def add_rating(self, rating: int) -> None:
        """
        Adds rating for the book if it does not exist in the rating 
        storage or appends it to the rating of the existing book.

        Args:
            rating: The rating of the book
        """
        book_isbn = rating.isbn
        if book_isbn in self._ratings.keys():
            self._ratings[book_isbn].append(rating)
        else:
            self._ratings[book_isbn] = [rating]

    def get_rating(self, book_isbn: int) -> List:
        """
        Retrieves all the ratings of the input book

        Args:
            book_isbn: The ISBN of the book
        
        Returns:
            all_ratings: List of all ratings for the book
        """
        all_ratings = []
        for rating in self._ratings.get(book_isbn):
            all_ratings.append(rating.rating)
        return all_ratings

    def get_rating_stats(self, book_isbn: int) -> int:
        """
        Calculates the rating statistics of the book by averaging
        across all the ratings of the book.

        Args:
            book_isbn: The ISBN of the book
        
        Returns:
            The rating stats of the book
        """
        all_ratings = self.get_rating(book_isbn)
        if len(all_ratings) == 1:
            rating_stats = all_ratings
        elif len(all_ratings) >1:
            rating_stats = sum(all_ratings)/len(all_ratings)
        else:
            rating_stats = 0
        return rating_stats