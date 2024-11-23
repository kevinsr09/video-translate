class DomainError(Exception):
    def __init__(self, mesagge: str, payload: str | None = None) -> None:
        super().__init__(mesagge)
        self.__mesagge: str = mesagge
        self.__payload: str = payload or ""

    @property
    def message(self) -> str:
        return self.__mesagge

    @property
    def payload(self) -> str:
        return self.__payload
