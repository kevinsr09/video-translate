from src.domain.entities.topic import Topic
from src.domain.repositories.topic_repository import TopicRepository
from src.infrastructure.config.envs import Envs
from src.infrastructure.lib.files import create_directory
from pathlib import Path


class LocalTopicRepository(TopicRepository):

    def __init__(self, envs: Envs) -> None:
        self.envs = envs

    def save(self, topic: Topic) -> None:
        path = Path(self.envs.path_folder()).joinpath(topic.name).__str__()
        create_directory(path_directory=path)
        return

    def search_all(self) -> list[Topic]:
        return [Topic("kevin")]
