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

# команда для функции поиска файлов в папке и во вложенных папках по регулярному выражению number_of_files
find_by_regex_parser = subparsers.add_parser('find', help='поиск файлов в папке по регулярному выражению')
find_by_regex_parser.add_argument('folder_path', help='путь к папке и имя папки')
find_by_regex_parser.add_argument('pattern', help='регулярное выражение')

# команда для функции добавления даты создания файла в название файла add_time_of_creation
add_time_of_creation_parser = subparsers.add_parser('add_date',
                                                    help='добавление даты создания файла в название файла')
add_time_of_creation_parser.add_argument('fof', help='путь к папке или файлу')
add_time_of_creation_parser.add_argument('--file', action='store_true',
                                         help='добавление даты создания файла в название указанного файла')
add_time_of_creation_parser.add_argument('--folder', action='store_true',
                                         help='добавление даты создания файла во все файлы в указанной папке, '
                                              'кроме файлов во вложенных папках ')
add_time_of_creation_parser.add_argument('--recursive', action='store_true',
                                         help='добавление даты создания файла в название файла '
                                              'во все файлы в папке и в файлы во вложенных папках')

# команда для функции analysis_of_folder
analysis_of_folder_parser = subparsers.add_parser('analysis',
                                                    help='Анализ всех вложенных папок и всех файлов внутри папки')
analysis_of_folder_parser.add_argument('fp', help='путь к папке')

args = parser.parse_args()

if args.command == 'copy':
    functions.copy_file(args.src, args.dst)
elif args.command == 'delete':
    functions.rm_file_or_folder(args.fof)
elif args.command == 'count':
    functions.number_of_files(args.folder_path)
elif args.command == 'find':
    functions.find_by_regex(args.folder_path, args.pattern)
elif args.command == 'add_date':
    if args.file:
        functions.add_time_of_creation_1(args.fof)
    if args.folder:
        functions.add_time_of_creation_2(args.fof)
    if args.recursive:
        functions.add_time_of_creation_3(args.fof)
elif args.command == 'analysis':
    functions.analysis_of_folder(args.fp)