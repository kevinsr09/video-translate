from collections.abc import Buffer
from src.domain.entities.video import Video
from src.domain.repositories.video_repository import VideoRepository


class VideoCreator:
    def __init__(self, repository: VideoRepository) -> None:
        self.repository = repository

    def create(self, name: str, topic_name: str, data: Buffer) -> None:
        video = Video(name, topic_name, data)
        self.repository.save(video)
