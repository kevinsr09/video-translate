from src.domain.repositories.topic_repository import TopicRepository
from src.domain.entities.topic import Topic


class TopicCreator:
    def __init__(self,  repository: TopicRepository) -> None:
        self.repository: TopicRepository = repository

    def create(self, name: str, description: str | None = None) -> None:
        topic = Topic.create(name)
        self.repository.save(topic)
        return
