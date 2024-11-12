from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from src.application.video.video_creator import VideoCreator
from src.infrastructure.repositories.local_video_repository import LocalVideoRepository, Envs
from typing import Annotated
video_creator = VideoCreator(LocalVideoRepository(Envs()))


video_router = APIRouter(
    prefix="/videos"
)


@video_router.get("")
def videos():
    return ["videos"]


@video_router.post("", status_code=201)
async def upload_video(file: Annotated[UploadFile, File()], topic_name: Annotated[str, Form()]):

    if file.filename == None:
        raise HTTPException(404, "Bad Request, add filename")

    try:

        name = file.filename
        topic_name = topic_name
        data = await file.read()

        video_creator.create(name, topic_name, data)

    except Exception as err:
        print(err)
        raise HTTPException(404, detail="error")
