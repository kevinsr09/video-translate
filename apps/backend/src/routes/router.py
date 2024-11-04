from fastapi import APIRouter
from src.routes.stt import stt_router
from src.routes.topic import topic_router
from src.routes.video import video_router

router = APIRouter()

router.include_router(router=stt_router, prefix="/api")
router.include_router(router=topic_router, prefix="/api")
router.include_router(router=video_router, prefix="/api")
