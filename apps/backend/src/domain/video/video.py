from src.domain.topic.topic_name import TopicName
from collections.abc import Buffer


class Video:

    def __init__(self, name: str, topic_name: str, data: Buffer | None = None):
        self.__name: str = name
        self.__topic_name: TopicName = TopicName(topic_name)
        self.__data: Buffer | None = data

    @staticmethod
    def create(name: str, topic_name: str) -> "Video":
        return Video(name, topic_name)

    @property
    def topic_name(self) -> str:
        return self.__topic_name.value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def data(self) -> Buffer | None:
        return self.__data

    def set_data(self, data: Buffer) -> None:
        self.__data = data
