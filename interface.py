import functions
import argparse

parser = argparse.ArgumentParser(prog='FAF manager', description='Менеджер файловой системы')

subparsers = parser.add_subparsers(help='Список команд')

# команда для функции копирования файла copy_file
copy_file_parser = subparsers.add_parser('copy', help='копирование файла')
copy_file_parser.add_argument('src', help='путь к исходному файлу и имя файла')
copy_file_parser.add_argument('dst', help='путь для копии файла и имя копии файла')
copy_file_parser.set_defaults(func=functions.copy_file)

args = parser.parse_args()

if copy_file_parser:
    functions.copy_file(args.src, args.dst)