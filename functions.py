import shutil
import pathlib
import os


def copy_file(src, dst):
    if pathlib.Path(src).exists():
        shutil.copy(src, dst)
    else:
        raise FileNotFoundError("Файл или папка не существует.")


def rm_file_or_folder(fof):
    if os.path.isfile(fof):
        os.remove(fof)
    elif os.path.isdir(fof):
        shutil.rmtree(fof)