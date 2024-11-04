from src.core.adapters.envs import envs
from src.core.lib.files import list_files


class TopicSearcherByName:
    def search(self, name: str):
        topics = list_files(envs.get("path_videos_folder"))
        index = topics.index(name)
        return topics[index]
