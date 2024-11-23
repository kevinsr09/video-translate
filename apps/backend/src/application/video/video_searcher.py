from collections.abc import Buffer
from src.domain.video.video import Video
from src.domain.video.video_repository import VideoRepository


class VideoSearcher:
    def __init__(self, repository: VideoRepository) -> None:
        self.repository = repository

    def search_all(self) -> list[Video]:
        return self.repository.search_all()
