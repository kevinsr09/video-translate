import os
from fastapi import APIRouter
from pydantic import BaseModel


class Folder(BaseModel):
    name: str
    description: str | None = None


videos_router = APIRouter()
videos = ["mysql", "postgress"]


@videos_router.get("")
def index():
    files = list_files("./videos")
    return files


@videos_router.post("/folder")
def create_folder(folder: Folder):
    result = create_directory(f"./videos/{folder.name}")
    return "created folder" if result else "not folder created"


@videos_router.get("/{id}")
def index(id):

    try:
        index_video = videos.index(id)
        video = videos[index_video]
    except:
        video = "not fount"
    finally:
        return video


def list_files(directory):
    try:
        # Obtener la lista de archivos y carpetas en el directorio
        return os.listdir(directory)
    except FileNotFoundError:
        print(f"Error: El directorio '{directory}' no se encuentra.")
        return []
    except PermissionError:
        print(f"Error: No tienes permiso para acceder a '{directory}'.")
        return []


def create_directory(directory):
    try:
        # Crea la carpeta, no da error si ya existe
        os.makedirs(directory, exist_ok=True)
        print(f"Carpeta '{directory}' creada exitosamente.")
        return True

    except Exception as e:
        print(f"Error al crear la carpeta '{directory}': {e}")
        return False
