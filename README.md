## <p style="text-align: center;">FAF менеджер</p>
FAF менеджер представляет собой учебный проект интерфейса командной строки, 
менеджера для файловой системы.  
  
Менеджер позволяет выполнять следующие команды:

* <span style="color:coral">copy</span> - команда, которая создает копию файла;
* <span style="color:coral">delete</span> - команда, которая удаляет файл или папку;
* <span style="color:coral">count</span> - команда, которая выводит общее количество файлов, находящиеся в папке и во вложенных папках;
* <span style="color:coral">find</span> - команда, которая выполняет поиск файла или файлов в папке по фильтру в виде регулярного выражения;
* <span style="color:coral">add_date</span> - команда, которая добавляет в названия файлов дату их создания:
  * при добавлении ключа <span style="color:coral">--file</span>, добавляет дату создания только для указанного файла;
  * при добавлении ключа <span style="color:coral">--folder</span>, добавляет дату создания в названия файлов в указанной папке, 
    кроме файлов во вложенных папках;
  * при добавлении ключа <span style="color:coral">--recursive</span>, добавляет дату создания в названия всех файлов в указанной папке,
    включая файлы во вложенных папках.
* <span style="color:coral">analysis</span> - команда, которая выводит название и полный размер указанной папки,
  названия и размеры всех вложенных папок в папку, 
  а также названия и размеры всех файлов внутри папки и вложенных папок.

### Запуск менеджера
Проект выполнен на версии Python 3.12.5.\
Запуск менеджера можно осуществить одним из двух способов:

<span style="color:lightgray">*_Способ 1_*</span>

Запустите командную строку и перейдите в каталог (папку) с файлами проекта.
Для запуска в командной строке введите **py interface.py**, или **python interface.py**, 
или **python3 interface.py** в зависимости от установленной версии или версий Python.

<span style="color:lightgray">*_Способ 2_*</span>

Запустите командную строку и перейдите в каталог (папку) с файлами проекта.
Затем в командной строке введите **faf**.\
Если запуска менеджера не происходит, воспользуетесь *способом 1*, либо откройте 
с помощью блокнота исполняемый файл *faf.bat* в папке с файлами проекта и замените
**py** на **python** или **python3**.  

### Примеры использования команд

#### <span style="color:coral">copy</span> 
Для того, чтобы скопировать файл, после введения основной команды необходимо передать два параметра: 

* путь к файлу и имя файла, который необходимо скопировать;  
* путь для копии файла и имя копии файла.

<span style="color:lightgray">_пример использования для копирования файла_:</span>   
<span style="color:lightblue">py interface.py copy C:\Users\user\Documents\file.txt C:\Users\user\Documents\copy_of_file.txt</span>  
или  
<span style="color:lightblue">faf copy C:\Users\user\Documents\file.txt C:\Users\user\Documents\copy_of_file.txt</span>

#### <span style="color:coral">delete</span> 
  
Для того, чтобы удалить файл или папку, после введения основной команды необходимо передать один параметр: 

* путь к файлу или к папке и имя файла или папки.  

<span style="color:lightgray">_пример использования для удаления папки_:</span>   
<span style="color:lightblue">py interface.py delete C:\Users\user\Documents\folder</span>  
или  
<span style="color:lightblue">faf delete C:\Users\user\Documents\folder</span>

#### <span style="color:coral">count</span> 
Для того, чтобы вывести общее количество файлов в папке, после введения основной команды необходимо передать параметр: 

* путь к папке и имя папки.  

<span style="color:lightgray">_пример использования для вывода количества файлов в папке_:</span>   
<span style="color:lightblue">py interface.py count C:\Users\user\Documents\folder</span>  
или  
<span style="color:lightblue">faf count C:\Users\user\Documents\folder</span>

#### <span style="color:coral">find</span> 
Для того, чтобы вывести общее количество файлов в папке, после введения основной команды необходимо передать два параметра: 

* путь к папке и имя папки;
* регулярное выражение.

<span style="color:lightgray">_пример использования для поиска в папке_:</span>   
<span style="color:lightblue">py interface.py find C:\Users\user\Documents\folder [a-z]</span>  
или  
<span style="color:lightblue">faf find C:\Users\user\Documents\folder [a-z]</span>

#### <span style="color:coral">add_date</span>

#### <span style="color:gray">- _добавление даты создания только в имя указанного файла_</span>  

Вводится основная команда <span style="color:coral">add_date</span> и ключ <span style="color:coral">--file</span>, а затем необходимо передать параметр: 

- - путь к файлу и имя файла.

<span style="color:lightgray">_пример использования для добавления даты создания только в имя указанного файла_:</span>   
<span style="color:lightblue">py interface.py add_date --file C:\Users\user\Documents\file.txt</span>  
или  
<span style="color:lightblue">faf add_date --file  C:\Users\user\Documents\file.txt</span>

#### <span style="color:gray">- _добавление даты создания в имена файлов в указанной папке, кроме файлов во вложенных папках_</span>  

Вводится основная команда <span style="color:coral">add_date</span> и ключ <span style="color:coral">--folder</span>, а затем необходимо передать параметр: 

- - путь к папке и имя папки.

<span style="color:lightgray">_пример использования для добавления даты создания в имена файлов в папке, 
кроме файлов во вложенных папках_:</span>   
<span style="color:lightblue">py interface.py add_date --folder C:\Users\user\Documents\folder</span>  
или  
<span style="color:lightblue">faf add_date --folder C:\Users\user\Documents\folder</span>

#### <span style="color:gray">- _добавление даты создания в названия файлов в указанной папке, включая файлы во вложенных папках_*</span>  

Вводится основная команда <span style="color:coral">add_date</span> и ключ <span style="color:coral">--recursive</span>, а затем необходимо передать параметр: 

- - путь к папке и имя папки.

<span style="color:lightgray">_пример использования для добавления даты создания в имена файлов в папке, 
включая файлы во вложенных папках_:</span>   
<span style="color:lightblue">py interface.py add_date --recursive C:\Users\user\Documents\folder</span>  
или  
<span style="color:lightblue">faf add_date --recursive C:\Users\user\Documents\folder</span>

#### <span style="color:coral">analysis</span> 
Для анализа папки вводится основная команда и передается параметр: 

* путь к папке и имя папки.  

<span style="color:lightgray">_пример использования для анализа папки_:</span>   
<span style="color:lightblue">py interface.py analysis C:\Users\user\Documents\folder</span>  
или  
<span style="color:lightblue">faf analysis C:\Users\user\Documents\folder</span>