from fastapi import APIRouter

stt_router = APIRouter()


@stt_router.get("")
def index():
    return "hello"
