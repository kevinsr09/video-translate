from fastapi import UploadFile
from os import path
from src.core.adapters.envs import envs
import shutil


def save_video(video: UploadFile, topic: str, name: str = ""):

    print(video.filename)
    file_location = path.join(
        envs.get("path_videos_folder"), topic, video.filename)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    return
