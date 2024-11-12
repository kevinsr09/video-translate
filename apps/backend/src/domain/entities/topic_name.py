from src.shared.domain.value_object import ValueObject


class TopicName[str](ValueObject):

    def __init__(self, name: str) -> None:
        self.__value = name

    @property
    def value(self) -> str:
        return self.__value
