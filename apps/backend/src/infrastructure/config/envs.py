from os import getenv


class Envs:

    @staticmethod
    def type_repository() -> str:
        return getenv('type_repository') or "local"

    @staticmethod
    def path_folder() -> str:
        return getenv('path_folder') or "./videos"
