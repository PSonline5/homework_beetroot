# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of
# Book class and adds the book to books list for current library.
# - group_by_author(author: Author) - returns a list of all books grouped by
# the specified author
# - group_by_year(year: int) - returns a list of all books grouped by the
# specified year

# All 3 classes must have a readable __repr__ method!

# Also, book class should have a class variable which holds the amount of
# all existing books


class Library:
    def __init__(self, name,):
        self.name = name
        self.books = []
        self.authors = []


class Book(Library):
    amount = 0

    def __init__(self, name, year, author):
        super().__init__(name)
        self.year = year
        self.author = author
        Book.amount += 1


class Author:
    def __init__(self, name, country, birthday):
        super().__init__(name)
        self.country = country
        self.birthday = birthday
        self.books = []



