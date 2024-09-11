from book import Book
from user import User
from library import Library

book1 = Book("Shoe dog","Phil Knight")
book2 = Book("Onegin","Pushkin")

user1 = User("Vanek")
user2 = User("Bob")

print(book1)
print(book2)
print(user1)
print(user2)

library1 = Library(user1, book1)
library2 = Library(user2, book2)

print(library1)
print(library2)
library1.write_to_file()
library2.write_to_file()
