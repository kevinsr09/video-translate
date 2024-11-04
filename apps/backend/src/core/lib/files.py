from os import listdir, mkdir


def list_files(directory):
    try:
        return listdir(directory)
    except FileNotFoundError:
        print(f"Error: El directorio '{directory}' no se encuentra.")
        return []
    except PermissionError:
        print(f"Error: No tienes permiso para acceder a '{directory}'.")
        return []


def create_directory(directory):
    try:
        mkdir(directory)
    except OSError as error:
        print(error)
        raise
