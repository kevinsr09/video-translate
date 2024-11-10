from os import listdir, mkdir


def list_files(directory: str) -> list[str]:
    try:
        return listdir(directory)
    except FileNotFoundError:
        print(f"Error: El directorio '{directory}' no se encuentra.")
        return []
    except PermissionError:
        print(f"Error: No tienes permiso para acceder a '{directory}'.")
        return []


def create_directory(path_directory: str) -> None:
    try:
        mkdir(path_directory)
    except OSError as error:
        print(error)
        raise
