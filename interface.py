import functions
import argparse

parser = argparse.ArgumentParser(prog='FAF manager', description='Менеджер файловой системы')

subparsers = parser.add_subparsers(help='Список команд')

# команда для функции копирования файла copy_file
copy_file_parser = subparsers.add_parser('copy_file', help='копирование файла')
copy_file_parser.add_argument('scr', help='исходный файл')
copy_file_parser.add_argument('dst', help='конечный файл')
copy_file_parser.set_defaults(func=functions.copy_file)

args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)