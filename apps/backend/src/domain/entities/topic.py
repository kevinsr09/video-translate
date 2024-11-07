class Topic():
    def __init__(self, name: str, description: str | None = None):
        self.__name: str = name
        self.__description: str | None = description

    @property
    def name(self):
        return self.__name
