import sys
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import functions

# создание основного окна
manager_window = tk.Tk()
manager_window.title("FAF manager")
manager_window.geometry("500x500")


# класс Перенаправитель вывода (в текстовый виджет)
class OutputRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)

    def flush(self):
        pass


# создание прокручиваемого текстового виджета
output_text = ScrolledText(wrap="none")
output_text.place(relx=0.5, anchor=tk.N, relwidth=0.9, relheight=0.5)
# добавление полосы прокрутки по горизонтали (по оси x)
h_scrollbar = ttk.Scrollbar(orient="horizontal", command=output_text.xview)
h_scrollbar.place(relx=0.5, rely=0.5, anchor=tk.N, relwidth=0.9)
output_text.configure(xscrollcommand=h_scrollbar.set)

# перенаправление вывода в экземпляр класса перенаправителя вывода
sys.stdout = OutputRedirector(output_text)
sys.stderr = OutputRedirector(output_text)


# функции-команды для кнопок
def add_toc():
    add_toc_window = tk.Toplevel()
    add_toc_window.title("Добавление даты создания в название файла или файлов")
    add_toc_window.geometry("500x200")
    add_to_file_btn = ttk.Button(add_toc_window, text="Добавить в выбранный файл", command=lambda: add_toc_1())
    add_to_file_btn.place(relx=0.29, rely=0.2, relwidth=0.42, relheight=0.2)
    add_to_files_btn = ttk.Button(add_toc_window, text="Добавить в файлы папки\n(кроме файлов вложенных папок)",
                                  command=lambda: add_toc_2())
    add_to_files_btn.place(relx=0.29, rely=0.4, relwidth=0.42, relheight=0.2)
    add_to_all_files_btn = ttk.Button(add_toc_window,
                                      text="Добавить во все файлы папки\n(включая файлы вложенных папок)",
                                      command=lambda: add_toc_3())
    add_to_all_files_btn.place(relx=0.29, rely=0.6, relwidth=0.42, relheight=0.2)


def add_toc_1():
    fof_path = filedialog.askopenfilename(title="Выберите файл")
    if fof_path:
        functions.add_time_of_creation_1(fof_path)
        print(f"Дата создания добавлена в название указанного файла:\n{fof_path}")


def add_toc_2():
    fof_path = filedialog.askdirectory(title="Выберите папку")
    if fof_path:
        functions.add_time_of_creation_2(fof_path)
        print(f"Дата создания добавлена в названия файлов указанной папки:\n{fof_path}")


def add_toc_3():
    fof_path = filedialog.askdirectory(title="Выберите папку")
    if fof_path:
        functions.add_time_of_creation_3(fof_path)
        print(f"Дата создания добавлена в названия файлов указанной папки:\n{fof_path}")


# команда для кнопки "Анализ папки"
def analysis():
    folder_path = filedialog.askdirectory(title="Выберите папку для анализа")
    if folder_path:
        functions.analysis_of_folder(folder_path)


# команда для кнопки "Копировать файл"
def copy_f():
    src_path = filedialog.askopenfilename(title="Выберите файл для копирования")
    if src_path:
        dst_path = filedialog.asksaveasfilename(title="Выберите путь для копии файла, введите имя и тип файла")
        if dst_path:
            functions.copy_file(src_path, dst_path)
            print(f'Файл, расположенный по следующему пути:\n{src_path}\nскопирован в указанный путь:\n{dst_path}')


# команда для кнопки "Поиск файлов"
def find_by_reg():
    folder_path = filedialog.askdirectory(title="Выберите папку для поиска файлов")
    if folder_path:
        find_by_reg_window = tk.Toplevel()
        find_by_reg_window.title("Поиск файлов")
        find_by_reg_window.geometry("250x150")
        regexp_entry = tk.Entry(find_by_reg_window)
        regexp_entry.place(relx=0.1, rely=0.1, relwidth=0.8)
        input_regexp_label = ttk.Label(find_by_reg_window, text="Введите регулярное выражение")
        input_regexp_label.place(relx=0.1, rely=0.23, relwidth=0.8)
        find_btn = ttk.Button(find_by_reg_window, text="Найти",
                              command=lambda: functions.find_by_regex(folder_path, pattern=regexp_entry.get()))
        find_btn.place(relx=0.5, rely=0.9, anchor=tk.S)


# команда для кнопки "Количество файлов"
def nof():
    folder_path = filedialog.askdirectory(title="Выберите папку для подсчета количества файлов в ней")
    if folder_path:
        functions.number_of_files(folder_path)


# команда для кнопки "Удалить"
def remove_fof():
    rm_window = tk.Toplevel()
    rm_window.title("Удаление файла или папки")
    rm_window.geometry("350x100")
    rm_file_btn = ttk.Button(rm_window, text="Удалить файл", command=lambda: remove_file())
    rm_file_btn.place(relx=0.32, rely=0.20, relwidth=0.36)
    rm_folder_btn = ttk.Button(rm_window, text="Удалить папку", command=lambda: remove_folder())
    rm_folder_btn.place(relx=0.32, rely=0.55, relwidth=0.36)


def remove_file():
    fof_path = filedialog.askopenfilename(title="Выберите файл")
    if fof_path:
        functions.rm_file_or_folder(fof_path)
        print(f"Файл по указанному пути:\n{fof_path}\nудален")


def remove_folder():
    fof_path = filedialog.askdirectory(title="Выберите папку")
    if fof_path:
        functions.rm_file_or_folder(fof_path)
        print(f"Папка по указанному пути:\n{fof_path}\nудалена")


# кнопки основного окна
# кнопка для очистки прокручиваемого текстового виджета
clear_text_btn = ttk.Button(text="Очистить", command=lambda: output_text.delete("1.0", "end"))
clear_text_btn.place(relx=0.92, rely=0.54, anchor=tk.NE)
# кнопка для закрытия окна приложения
exit_btn = ttk.Button(text="Выход", command=manager_window.destroy)
exit_btn.place(relx=0.99, rely=0.99, anchor=tk.SE)
# кнопка для вызова функции analysis_of_folder
analysis_btn = ttk.Button(text="Анализ папки", command=lambda: analysis())
analysis_btn.place(relx=0.359, rely=0.61, relwidth=0.282)
# кнопка для вызова группы функций add_time_of_creation
add_date_of_creation_btn = ttk.Button(text="Добавить дату создания", command=lambda: add_toc())
add_date_of_creation_btn.place(relx=0.359, rely=0.66, relwidth=0.282)
# кнопка для вызова функции number_of_files
nof_btn = ttk.Button(text="Количество файлов", command=lambda: nof())
nof_btn.place(relx=0.359, rely=0.71, relwidth=0.282)
# кнопка для вызова функции copy_file
copy_btn = ttk.Button(text="Копировать файл", command=lambda: copy_f())
copy_btn.place(relx=0.359, rely=0.76, relwidth=0.282)
# кнопка для вызова функции find_by_regex
find_by_regex_btn = ttk.Button(text="Поиск файлов", command=lambda: find_by_reg())
find_by_regex_btn.place(relx=0.359, rely=0.81, relwidth=0.282)
# кнопка для вызова функции rm_file_or_folder
remove_btn = ttk.Button(text="Удалить", command=lambda: remove_fof())
remove_btn.place(relx=0.359, rely=0.86, relwidth=0.282)

manager_window.mainloop()

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
