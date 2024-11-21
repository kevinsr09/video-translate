from .topic_name import TopicName


class Topic():
    def __init__(self, name: str, description: str | None = None):
        self.__name: TopicName = TopicName(name)
        self.__description: str | None = description

    @property
    def name(self) -> str:
        return self.__name.value

    @property
    def description(self):
        return self.__description

    def to_primitives(self) -> dict[str, str]:
        return {"name": self.name, "description": self.description or ""}

    @staticmethod
    def from_primitives(name: str, description: str | None = None) -> "Topic":
        return Topic(name, description)

    @staticmethod
    def create(name: str, description: str | None = None) -> "Topic":
        return Topic(name, description)
