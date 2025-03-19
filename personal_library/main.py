import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""
    
    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage"""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()
        
        def read_from_file(self):
            """Load saved books from a JSON file into memory.
            If the file doesn't exist or is corrupted, start with an empty collection."""