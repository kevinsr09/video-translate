from pathlib import Path
from src.core.adapters.envs import envs
from src.core.lib.files import list_files


class TopicSearcherAll:

    def search(self):
        return list_files(envs.get("path_videos_folder"))
