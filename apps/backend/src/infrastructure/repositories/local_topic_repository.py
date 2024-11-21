from src.domain.topic.topic import Topic
from src.domain.topic.topic_repository import TopicRepository
from src.infrastructure.config.envs import Envs
from src.infrastructure.lib.files import create_directory, list_files
from pathlib import Path


class LocalTopicRepository(TopicRepository):

    def __init__(self, envs: Envs) -> None:
        self.envs = envs

    def save(self, topic: Topic) -> None:
        path = Path(self.envs.path_folder()).joinpath(topic.name).__str__()
        create_directory(path_directory=path)
        return

    def search_all(self) -> list[Topic]:
        topics_primitives = list_files(self.envs.path_folder())
        topics = [Topic(topic) for topic in topics_primitives]

        return topics

    def search_by_name(self, name: str) -> Topic:
        topic_primitive = list_files(self.envs.path_folder())
        topic_primitive.index(name)
        return Topic(name)
