import sys
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import functions

# создание окна
manager_window = tk.Tk()
manager_window.title("FAF manager")
manager_window.geometry("500x500")


# класс перенаправитель вывода (в текстовый виджет)
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


#
def add_doc():
    pass


# команда для кнопки "Анализ папки"
def analysis():
    folder_path = filedialog.askdirectory()
    functions.analysis_of_folder(folder_path)


# команда для кнопки "Копировать файл"
def copy_f():
    src_path = filedialog.askopenfilename(title="Выберите файл для копирования")
    dst_path = filedialog.asksaveasfilename(title="Выберите путь для копии файла, введите имя и тип файла")
    functions.copy_file(src_path, dst_path)
    print(f'Файл, расположенный по следующему пути: {src_path} успешно скопирован в указанный путь: {dst_path}')


# команда для кнопки "Поиск файлов"
def find_by_reg():
    folder_path = filedialog.askdirectory()
    find_by_reg_window = tk.Tk()
    find_by_reg_window.title("Поиск файлов")
    find_by_reg_window.geometry("250x150")
    regexp_entry = tk.Entry(find_by_reg_window)
    regexp_entry.place(relx=0.5, rely=0.1, anchor=tk.N, relwidth=0.8)
    input_regexp_label = ttk.Label(find_by_reg_window, text="Введите регулярное выражение")
    input_regexp_label.place(relx=0.5, rely=0.2, anchor=tk.N, relwidth=0.8)
    find_btn = ttk.Button(find_by_reg_window, text="Найти",
                          command=lambda: functions.find_by_regex(folder_path, pattern=regexp_entry.get()))
    find_btn.place(relx=0.5, rely=0.9, anchor=tk.S)


# команда для кнопки "Количество файлов"
def nof():
    folder_path = filedialog.askdirectory()
    functions.number_of_files(folder_path)


# команда для кнопки "Удалить"
def remove_fof():
    fof_path = filedialog.askopenfilename()
    functions.rm_file_or_folder(fof_path)


# кнопки
# кнопка для очистки прокручиваемого текстового виджета
clear_text_btn = ttk.Button(text="Очистить", command=lambda: output_text.delete("1.0", "end"))
clear_text_btn.place(relx=0.92, rely=0.54, anchor=tk.NE)
# кнопка для закрытия окна приложения
exit_btn = ttk.Button(text="Выход", command=manager_window.destroy)
exit_btn.place(relx=0.99, rely=0.99, anchor=tk.SE)
# кнопка для вызова функции analysis_of_folder
analysis_btn = ttk.Button(text="Анализ папки", command=lambda: analysis())
analysis_btn.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
# кнопка для вызова функции number_of_files
nof_btn = ttk.Button(text="Количество файлов", command=lambda: nof())
nof_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
# кнопка для вызова функции find_by_regex
find_by_regex_btn = ttk.Button(text="Поиск файлов", command=lambda: find_by_reg())
find_by_regex_btn.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
# кнопка для вызова функции copy_file
copy_btn = ttk.Button(text="Копировать файл", command=lambda: copy_f())
copy_btn.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
# кнопка для вызова функции rm_file_or_folder
delete_btn = ttk.Button(text="Удалить", command=lambda: remove_fof())
delete_btn.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
# кнопка для вызова группы функций add_time_of_creation
add_date_of_creation_btn = ttk.Button(text="Добавить дату создания", command=lambda: add_doc())
add_date_of_creation_btn.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

manager_window.mainloop()
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
