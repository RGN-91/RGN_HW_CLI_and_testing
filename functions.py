import shutil
import pathlib


def copy_file(src, dst):
    if pathlib.Path(src).exists():
        shutil.copy(src, dst)
    else:
        raise FileNotFoundError("Файл или папка не существует.")
