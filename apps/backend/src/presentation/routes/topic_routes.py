from fastapi import APIRouter, HTTPException
from src.application.topic.topic_creator import TopicCreator
from src.application.topic.topic_searcher import TopicSearcher
from src.shared.domain.domain_error import DomainError
from src.infrastructure.repositories.local_topic_repository import LocalTopicRepository, Envs
from pydantic import BaseModel

topic_repository = LocalTopicRepository(Envs())
topic_creator = TopicCreator(topic_repository)
topic_searcher = TopicSearcher(topic_repository)


topic_router = APIRouter(
    prefix="/topics"
)


@topic_router.get("")
def topics():
    try:
        topics = topic_searcher.search_all()
        topics_primitives = [topic.to_primitives() for topic in topics]
        return topics_primitives

    except:
        raise HTTPException(status_code=404, detail="Topics not found")


@topic_router.get("/{name}")
def topic_for_name(name: str):
    try:
        return topic_searcher.search_by_name(name).to_primitives()
    except:
        raise HTTPException(status_code=404, detail="Topic not found")


class TopicRequestModel(BaseModel):
    name: str
    description: str | None = None


@topic_router.post("", status_code=201)
def topic_create(topic: TopicRequestModel):
    try:
        topic_creator.create(topic.name)
        return

    except DomainError as err:
        print(err)
        detail = {"mesagge": f"{err.message}", "payload": f"{err.payload}"}
        raise HTTPException(status_code=400, detail=detail)

    except Exception as err:
        print(err)
        raise HTTPException(status_code=409, detail="Topic alredy exist")


@topic_router.get("/{name}/videos")
def topic_videos(name: str):
    return []
