from abc import ABCMeta, abstractmethod
from src.domain.entities.video import Video


class VideoRepository(metaclass=ABCMeta):

    @abstractmethod
    def save(self, video: Video) -> None:
        pass

    # @abstractmethod
    # def search_all() -> list[Video]:
    #     pass

    # @abstractmethod
    # def search_by_name(self, name: str) -> Topic:
    #     pass
