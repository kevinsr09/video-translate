from src.domain.topic.topic_repository import TopicRepository
from src.domain.topic.topic import Topic


class TopicCreator:
    def __init__(self,  repository: TopicRepository) -> None:
        self.repository: TopicRepository = repository

    def create(self, name: str, description: str | None = None) -> None:
        topic = Topic.create(name)
        self.repository.save(topic)
        return
