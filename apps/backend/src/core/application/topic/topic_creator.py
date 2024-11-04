from src.core.lib.files import create_directory
from src.core.adapters.envs import envs


class TopicCreator:
    def create(self, name: str):
        create_directory(envs.get("path_videos_folder")+"/"+name)
        return
