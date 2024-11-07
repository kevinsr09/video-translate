from src.domain.entities.topic import Topic
from src.domain.repositories.topic_repository import TopicRepository


class TopicSearcher():
    def __init__(self, repository) -> None:
        self.repository: TopicRepository = repository

    def search_all(self) -> list[Topic]:
        return self.repository.search_all()
