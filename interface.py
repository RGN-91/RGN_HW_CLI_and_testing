import functions
import argparse

parser = argparse.ArgumentParser(prog='FAF manager', description='Менеджер файловой системы')

subparsers = parser.add_subparsers(dest='command', help='Список команд')

# команда для функции копирования файла copy_file
copy_file_parser = subparsers.add_parser('copy', help='копирование файла')
copy_file_parser.add_argument('src', help='путь к исходному файлу и имя файла')
copy_file_parser.add_argument('dst', help='путь для копии файла и имя копии файла')

# команда для функции удаления файла или папки rm_file_or_folder
rm_file_or_folder_parser = subparsers.add_parser('delete', help='удаление файла или папки')
rm_file_or_folder_parser.add_argument('fof', help='путь к файлу или к папке и имя')

# команда для функции подсчета количества файлов в папке и во вложенных папках при их наличии number_of_files
number_of_files_parser = subparsers.add_parser('count', help='количество файлов в папке и папках папки')
number_of_files_parser.add_argument('folder_path', help='путь к папке и имя папки')

args = parser.parse_args()

if args.command == 'copy':
    functions.copy_file(args.src, args.dst)
elif args.command == 'delete':
    functions.rm_file_or_folder(args.fof)
elif args.command == 'count':
    functions.number_of_files(args.folder_path)