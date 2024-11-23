import re
from src.shared.domain.value_objects.string_value_object import StringValueObject
from .topic_name_invalid_length_error import TopicNameInvalidLengthError
from .topic_name_invalid_characters_error import TopicNameInvalidCharactersError

errors_map = {
    "is_valid_length": "The length of the topic name must be greater than or equal to 3 characters",
    "invalid_characters": "The topic name can only contain letters, numbers, and hyphens"
}


class TopicName(StringValueObject):

    def __init__(self, name: str) -> None:

        self.is_valid_length(name)
        self.is_valid_characters(name)
        super().__init__(name)

    def is_valid_length(self, name: str) -> None:
        if (len(name) < 3):
            raise TopicNameInvalidLengthError(
                errors_map["is_valid_length"], name)

    def is_valid_characters(self, name: str) -> None:
        if not re.match(self.pattern(), name):
            raise TopicNameInvalidCharactersError(
                errors_map["invalid_characters"], name)

    @classmethod
    def pattern(cls):
        return r'^[A-Za-z0-9][A-Za-z0-9-]*[A-Za-z0-9]$'
