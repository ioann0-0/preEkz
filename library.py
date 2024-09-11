from book import Book
from user import User
import json

class Library:
    def __init__(self, user, book):
        self.__book = book
        self.__user = user

    def write_to_file(self):
        with open ("library.txt","w", encoding = "utf-8") as file:
            writetable_data = {"user": {"name": self.__user.name},"book":{"author":self.__book.author,"title": self.__book.title}}
            json.dump(writetable_data, file)
        with open ("library.txt","a", encoding = "utf-8") as file:
            writetable_data = {"user": {"name": self.__user.name},"book":{"author":self.__book.author,"title": self.__book.title}}
            json.dump(writetable_data, file)    


    def __str__(self) -> str:
        return f"книгу {self.__book.title} {self.__book.author} забрал {self.__user.name}"
