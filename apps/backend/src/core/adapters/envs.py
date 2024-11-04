from os import getenv

envs = {
    "path_videos_folder": getenv('path_videos_folder') or "./videos"
}
