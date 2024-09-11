class User:
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self) -> str:
        return f"Your name: {self.__name}"
