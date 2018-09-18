import operator

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

    def __repr__(self):
        return  "User " +  self.name + ", email: " + self.email + ", books read : " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        return False

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        rated_books = 0
        total_rating = 0
        for value in self.books.values():
            if value != None:
                rated_books += 1
                total_rating += value
        if rated_books == 0:
            return None
        return total_rating / rated_books

    def __hash__(self):
        return hash((self.name, self.email))

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The ISBN for " + str(self.title) + " has been updated to " + str(self.isbn))

    def add_rating(self, rating):
        if rating != None:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title

    def get_average_rating(self):
        total_rating = 0
        for rating in self.ratings:
            total_rating += rating
        if len(self.ratings) == 0:
            return None
        return total_rating / len(self.ratings)


class Fiction(Book):
    def __init__(self, title, author ,isbn ):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return self.title + " by " + self.author


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level():
        return self.level

    def __repr__(self):
        return  self.title + ", a " + self.level + " manual on " + self.subject


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction = Fiction(title, author, isbn)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email " + email + "!")

    def add_user(self, name, email, books = None):
        user = User(name, email)
        self.users[email] = user
        if books != None:
            for book in books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        max_value = float("-inf")
        max_key = None
        for key, value in self.books.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key

    def highest_rated_book(self):
        max_rating = float("-inf")
        max_key = None
        for key in self.books.keys():
            rating = key.get_average_rating()
            if rating > max_rating:
                max_rating = rating
                max_key = key
        return max_key

    def most_positive_user(self):
        max_rating = float("-inf")
        max_value = None
        for value in self.users.values():
            rating = value.get_average_rating()
            if rating > max_rating:
                 max_rating = rating
                 max_value = value
        return max_value

    def get_n_most_read_books(self, n):
        sorted_list = (sorted(self.books.items(), key=operator.itemgetter(1), reverse=True)[:n])
        return_list = []
        for tupel in sorted_list:
            return_list.append(tupel[0])
        return return_list

    def get_n_most_prolific_readers (self, n):
        tmp_dict = {}
        for value in self.users.values():
            book_count = len(value.books)
            tmp_dict[value] = book_count
        sorted_list = (sorted(tmp_dict.items(), key=operator.itemgetter(1), reverse=True)[:n])
        return_list = []
        for tupel in sorted_list:
            return_list.append(tupel[0])
        return return_list














