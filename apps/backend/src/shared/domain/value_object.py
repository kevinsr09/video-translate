from abc import ABCMeta, abstractmethod


class ValueObject[T](metaclass=ABCMeta):

    @abstractmethod
    def value(self) -> T:
        pass
