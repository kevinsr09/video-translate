from fastapi import APIRouter, File, UploadFile, HTTPException
from src.core.application.video.save import save_video

video_router = APIRouter(
    prefix="/videos"
)


@video_router.get("")
def videos():
    return ["videos"]


@video_router.post("", status_code=201)
def upload_video(file: UploadFile = File(...)):
    try:
        save_video(video=file, topic="kevin")
        return
    except Exception as err:
        print(err)
        raise HTTPException(400, detail="error")
