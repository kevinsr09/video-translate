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


def list_all_videos(path: str):
    topics = list_files(path)
    topics_dir = map(lambda v: f"{path}/{v}", topics)

    return []


def get_videos_from_directory(directory):
    try:
        # Lista los archivos en el directorio
        # Solo consideramos archivos que no sean directorios y que tengan extensión de video (por ejemplo, .mp4)
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith(('.mp4', '.mkv', '.avi'))]
    except FileNotFoundError:
        print(f"El directorio {directory} no existe.")
        return []
