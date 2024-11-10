from abc import ABCMeta, abstractmethod
from src.domain.entities.topic import Topic


class TopicRepository(metaclass=ABCMeta):

    @abstractmethod
    def save(self, topic: Topic) -> None:
        pass

    @abstractmethod
    def search_all() -> list[Topic]:
        pass

    @abstractmethod
    def search_by_name(self, name: str) -> Topic:
        pass
