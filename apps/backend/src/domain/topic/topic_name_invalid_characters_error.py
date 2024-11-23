from src.shared.domain.domain_error import DomainError


class TopicNameInvalidCharactersError(DomainError):
    def __init__(self, mesagge: str, payload: str | None = None) -> None:
        super().__init__(mesagge, payload)
