from .value_object import ValueObject


class StringValueObject(ValueObject[str]):
    def __init__(self, value: str) -> None:
        self.__value: str = value

    @property
    def value(self) -> str:
        return self.__value
