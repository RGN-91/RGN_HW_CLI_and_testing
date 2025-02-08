import shutil
import pathlib
import os
import re
import datetime


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


def add_time_of_creation_1(fof):
    """Функция, которая добавляет в название указанного файла дату его создания."""
    if os.path.isfile(fof):
        file_tc = os.path.getctime(fof)
        file_tc = datetime.date.fromtimestamp(file_tc)
        file_tc = file_tc.strftime("%Y-%m-%d")
        fnp_lst = fof.rsplit(sep=".")
        file_name = "".join(fnp_lst[:-1])
        file_ext = "".join(fnp_lst[-1:])
        os.replace(fof, file_name + " " + file_tc + "." + file_ext)
    else:
        raise FileNotFoundError("Указанный файл не существует.")


def add_time_of_creation_2(fof):
    """
    Функция, которая добавляет в названия файлов в указанной папке дату создания файла,
    кроме файлов во вложенных папках.
    """
    if os.path.isdir(fof):
        files_lst = [file for file in os.listdir(fof) if os.path.isfile(os.path.join(fof, file))]
        for file in files_lst:
            file_tc = os.path.getctime(os.path.join(fof, file))
            file_tc = datetime.date.fromtimestamp(file_tc)
            file_tc = file_tc.strftime("%Y-%m-%d")
            fnp_lst = file.rsplit(sep=".")
            file_name = "".join(fnp_lst[:-1])
            file_ext = "".join(fnp_lst[-1:])
            os.replace(os.path.join(fof, file), os.path.join(fof, file_name + " " + file_tc + "." + file_ext))
    else:
        raise NotADirectoryError("Указанная папка не существует.")


def add_time_of_creation_3(fof):
    """
    Функция, которая добавляет в названия всех файлов в указанной папке дату создания файла,
    включая файлы во вложенных папках.
    """
    if os.path.isdir(fof):
        for dp, dn, files in os.walk(fof):
            for file in files:
                file_tc = os.path.getctime(os.path.join(dp, file))
                file_tc = datetime.date.fromtimestamp(file_tc)
                file_tc = file_tc.strftime("%Y-%m-%d")
                fnp_lst = file.rsplit(sep=".")
                file_name = "".join(fnp_lst[:-1])
                file_ext = "".join(fnp_lst[-1:])
                os.replace(os.path.join(dp, file), os.path.join(dp, file_name + " " + file_tc + "." + file_ext))
    else:
        raise NotADirectoryError("Указанная папка не существует.")
