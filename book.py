class Book:
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    def __str__(self) -> str:
        return f"{self.__title} {self.__author}"

# onebook = Book("продавец обуви","Фил Найт")
# print(onebook.__str__())
