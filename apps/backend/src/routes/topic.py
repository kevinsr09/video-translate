from fastapi import APIRouter, HTTPException
from src.core.entities.Topic import Topic
from src.core.application.topic.topic_searcher_all import TopicSearcherAll
from src.core.application.topic.topic_searcher_by_name import TopicSearcherByName
from src.core.application.topic.topic_creator import TopicCreator


topic_router = APIRouter(
    prefix="/topics"
)


@topic_router.get("")
def topics():
    return TopicSearcherAll().search()


@topic_router.get("/{name}")
def topic_for_id(name: str):
    try:
        return TopicSearcherByName().search(name)
    except:
        raise HTTPException(status_code=404, detail="Topic not found")


@topic_router.post("", status_code=201)
def topic_create(topic: Topic):
    try:
        TopicCreator().create(topic.name)
        return
    except:
        raise HTTPException(status_code=409, detail="Topic alredy exist")
