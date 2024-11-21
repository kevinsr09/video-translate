from src.domain.topic.topic import Topic
from src.domain.topic.topic_repository import TopicRepository


class TopicSearcher():
    def __init__(self, repository) -> None:
        self.repository: TopicRepository = repository

    def search_all(self) -> list[Topic]:
        return self.repository.search_all()

    def search_by_name(self, name: str) -> Topic:
        return self.repository.search_by_name(name)
