import os
import shutil
import re
import datetime


def copy_file(src, dst):
    """
    Функция, которая копирует файл.
    src - путь к файлу, который будет скопирован
    dst - путь для копии файла
    """
    if os.path.isfile(src):
        shutil.copy(src, dst)
    else:
        raise FileNotFoundError("Указанный файл не существует.")


def rm_file_or_folder(fof):
    """
    Функция, которая удаляет файл или папку.
    fof - путь к файлу или к папке
    """
    if os.path.isfile(fof):
        os.remove(fof)
    elif os.path.isdir(fof):
        shutil.rmtree(fof)


def number_of_files(folder_path):
    """
    Функция, которая выводит общее количество файлов, которые находятся в папке и во вложенных папках.
    folder_path - путь к папке
    """
    if os.path.isdir(folder_path):
        print(sum([len(files) for dp, dn, files in os.walk(folder_path)]))
    else:
        raise NotADirectoryError("Указанная папка не существует.")


def find_by_regex(folder_path, pattern):
    """
    Функция, которая осуществляет поиск файла или файлов в папке по фильтру в виде регулярного выражения.
    folder_path - путь к папке
    pattern - регулярное выражение
    """
    if os.path.isdir(folder_path):
        regex = re.compile(pattern)
        for dp, dn, files in os.walk(folder_path):
            for file in files:
                if regex.match(file):
                    print(file)
    else:
        raise NotADirectoryError("Указанная папка не существует.")


def add_time_of_creation_1(fof):
    """
    Функция, которая добавляет в название указанного файла дату его создания.
    fof - путь к файлу
    """
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
    fof - путь к папке
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
    fof - путь к папке
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


def analysis_of_folder(fp):
    """
    Функция, которая определяет и выводит название и полный размер папки,
    названия и размеры всех вложенных папок в папку,
    а также названия и размеры всех файлов внутри папки и вложенных папок.
    fp - путь к папке
    """

    if os.path.isdir(fp):
        # Определение полного размера папки
        full_size = 0
        for dp, drn, fn in os.walk(fp):
            for file in fn:
                full_size += os.path.getsize(os.path.join(dp, file))
        if 1024 ** 4 > full_size >= 1024 ** 3:
            print(f'Полный размер папки {os.path.basename(fp)}: {full_size / 1024 ** 3:.1f} Гб')
        elif 1024 ** 3 > full_size >= 1024 ** 2:
            print(f'Полный размер папки {os.path.basename(fp)}: {full_size / 1024 ** 2:.1f} Мб')
        elif 1024 ** 2 > full_size >= 1024:
            print(f'Полный размер папки {os.path.basename(fp)}: {full_size / 1024:.1f} Кб')
        else:
            print(f'Полный размер папки {os.path.basename(fp)}: {full_size} байт')
        # Вложенные папки и определение их размеров
        fsf_lst = [x[0] for x in os.walk(fp)]
        # удаляем основную папку из списка
        del fsf_lst[0]
        print("- Вложенные папки и их размеры:")
        for folder in fsf_lst:
            fld_size = 0
            for dp, drn, fn in os.walk(folder):
                for file in fn:
                    fld_size += os.path.getsize(os.path.join(dp, file))
            if 1024 ** 4 > fld_size >= 1024 ** 3:
                print(f'{os.path.basename(folder.rsplit("/")[-1])} {fld_size / 1024 ** 3:.1f} Гб')
            elif 1024 ** 3 > fld_size >= 1024 ** 2:
                print(f'{os.path.basename(folder.rsplit("/")[-1])} {fld_size / 1024 ** 2:.1f} Мб')
            elif 1024 ** 2 > fld_size >= 1024:
                print(f'{os.path.basename(folder.rsplit("/")[-1])} {fld_size / 1024:.1f} Кб')
            else:
                print(f'{os.path.basename(folder.rsplit("/")[-1])} {fld_size} байт')
        # Файлы в папке и во вложенных папках и определение размеров файлов
        print("-- Файлы в папке и во вложенных папках и размеры файлов:")
        for dp, drn, fn in os.walk(fp):
            for file in fn:
                file_size = 0
                file_size += os.path.getsize(os.path.join(dp, file))
                if 1024 ** 4 > file_size >= 1024 ** 3:
                    print(f'{file} {file_size / 1024 ** 3:.1f} Гб')
                elif 1024 ** 3 > file_size >= 1024 ** 2:
                    print(f'{file} {file_size / 1024 ** 2:.1f} Мб')
                elif 1024 ** 2 > file_size >= 1024:
                    print(f'{file} {file_size / 1024:.1f} Кб')
                else:
                    print(f'{file} {file_size} байт')
    else:
        raise NotADirectoryError("Указанная папка не существует.")
