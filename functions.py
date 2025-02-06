import shutil
import pathlib
import os
import re


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


def number_of_files(folder_path):
    """Выводит общее количество файлов в папке и во вложенных папках"""
    print(sum([len(files) for dp, dn, files in os.walk(folder_path)]))


def find_by_regex(folder_path, pattern):
    regex = re.compile(pattern)
    for dp, dn, files in os.walk(folder_path):
        for file in files:
            if regex.match(file):
                print(file)
