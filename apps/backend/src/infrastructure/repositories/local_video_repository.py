from src.domain.video.video import Video
from src.domain.video.video_repository import VideoRepository
from src.infrastructure.config.envs import Envs
from src.infrastructure.lib.files import create_directory, list_files
from pathlib import Path


class LocalVideoRepository(VideoRepository):

    def __init__(self, envs: Envs) -> None:
        self.envs = envs

    def save(self, video: Video) -> None:

        if video.data == None:
            raise

        path = Path(self.envs.path_folder()).joinpath(
            video.topic_name).joinpath(video.name).__str__()

        with open(path, "wb") as f:

            f.write(video.data)

        return

    # def search_all(self) -> list[Video]:
    #     videos_primitives = list_files(self.envs.path_folder())
    #     videos = [Video(video) for video in videos_primitives]

    #     return videos

    # def search_by_name(self, name: str) -> video:
    #     video_primitive = list_files(self.envs.path_folder())
    #     video_primitive.index(name)
    #     return video(name)
