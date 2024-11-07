from fastapi import APIRouter, HTTPException
from src.application.topic.topic_creator import TopicCreator
from src.application.topic.topic_searcher import TopicSearcher

from src.infrastructure.repositories.local_topic_repository import LocalTopicRepository, Envs


topic_repository = LocalTopicRepository(Envs())
topic_creator = TopicCreator(topic_repository)
topic_searcher = TopicSearcher(topic_repository)


topic_router = APIRouter(
    prefix="/topics"
)


@topic_router.get("")
def topics():
    return topic_searcher.search_all()


# @topic_router.get("/{name}")
# def topic_for_id(name: str):
#     try:
#         return TopicSearcherByName().search(name)
#     except:
#         raise HTTPException(status_code=404, detail="Topic not found")


# @topic_router.post("", status_code=201)
# def topic_create(topic: Topic):
#     try:
#         TopicCreator().create(topic.name)
#         return
#     except:
#         raise HTTPException(status_code=409, detail="Topic alredy exist")
