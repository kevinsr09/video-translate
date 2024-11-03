from fastapi import APIRouter
from src.routes.api.stt import stt_router
from src.routes.api.videos import videos_router
router = APIRouter()

router.include_router(router=stt_router, prefix="/api/stt")
router.include_router(router=videos_router, prefix="/api/videos")
