import unittest
import functions
import pathlib
import os
import shutil
import contextlib
import io
import datetime


class TestFaF(unittest.TestCase):
    # тестирование функции copy_file
    def test_feature_1(self):
        test_file_1 = open('test_1.txt', 'a+')
        test_file_1.close()
        functions.copy_file('test_1.txt', 'test_1_copy.txt')
        path_of_copy = pathlib.Path('test_1_copy.txt')
        self.assertEqual((str(path_of_copy), path_of_copy.is_file()), (str(path_of_copy), True))
        os.remove('test_1.txt')
        os.remove('test_1_copy.txt')
        with self.assertRaises(FileNotFoundError):
            functions.copy_file('test_1.txt', 'test_1_copy.txt')

    # тестирование функции rm_file_or_folder
    def test_feature_2(self):
        test_file_2 = open('test_2.txt', 'a+')
        test_file_2.close()
        os.mkdir('test_folder')
        path_of_file = pathlib.Path('test_2.txt')
        path_of_folder = pathlib.Path('test_folder')
        self.assertTrue(os.path.exists(path_of_file))
        self.assertTrue(os.path.exists(path_of_folder))
        functions.rm_file_or_folder('test_2.txt')
        functions.rm_file_or_folder('test_folder')
        self.assertFalse(os.path.exists(path_of_file))
        self.assertFalse(os.path.exists(path_of_folder))

    def test_feature_3(self):
        """тестирует функцию number_of_files для подсчета файлов в папке и во вложенных папках"""
        os.mkdir('test_folder_2')
        os.chdir('test_folder_2')
        test_file_3 = open('test_3.txt', 'a+')
        test_file_3.close()
        test_file_4 = open('test_4.txt', 'a+')
        test_file_4.close()
        os.mkdir('test_folder_3')
        os.chdir('test_folder_3')
        test_file_5 = open('test_5.txt', 'a+')
        test_file_5.close()
        os.chdir('..')
        os.chdir('..')
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            functions.number_of_files('test_folder_2')
        output = f.getvalue()
        self.assertEqual(int(output), 3)
        shutil.rmtree('test_folder_2')

    def test_feature_4(self):
        """
        тестирует find_by_regex функцию, которая осуществляет поиск файлов
        в папке и во вложенных папках с помощью регулярных выражений
        """
        os.mkdir('test_folder_4')
        os.chdir('test_folder_4')
        test_file_6 = open('123.txt', 'a+')
        test_file_6.close()
        test_file_7 = open('abc.txt', 'a+')
        test_file_7.close()
        os.mkdir('test_folder_5')
        os.chdir('test_folder_5')
        test_file_8 = open('def.txt', 'a+')
        test_file_8.close()
        test_file_9 = open('456.txt', 'a+')
        test_file_9.close()
        os.chdir('..')
        os.chdir('..')
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            functions.find_by_regex('test_folder_4', '[0-9]')
        output_1 = f.getvalue().splitlines()
        self.assertEqual(output_1, ["123.txt", "456.txt"])
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            functions.find_by_regex('test_folder_4', '[a-z]')
        output_2 = f.getvalue().splitlines()
        self.assertEqual(output_2, ["abc.txt", "def.txt"])
        shutil.rmtree('test_folder_4')

    def test_feature_5a(self):
        """
        Тестирует add_time_of_creation_1 функцию на следующее:
        - на появление ошибки, если передано название файла, которого не существует;
        - на добавление даты создания файла в название указанного файла.
        """
        with self.assertRaises(FileNotFoundError):
            functions.add_time_of_creation_1('nonexistent_file.txt')
        os.mkdir('test_folder_6')
        os.chdir('test_folder_6')
        test_file_9 = open('dc.txt', 'a+')
        test_file_9.close()
        date_of_creation = datetime.datetime.today().strftime("%Y-%m-%d")
        fn_with_dc = 'dc' + ' ' + date_of_creation + '.txt'
        functions.add_time_of_creation_1('dc.txt')
        self.assertTrue(os.path.isfile(fn_with_dc))
        os.chdir('..')
        shutil.rmtree('test_folder_6')

    def test_feature_5b(self):
        """
        Тестирует add_time_of_creation_2 функцию на следующее:
        - на появление ошибки, если передано название папки, которой не существует;
        - на добавление даты создания файла в названия всех файлов,
        которые находятся в указанной папке, кроме файлов во вложенных папках.
        """
        with self.assertRaises(NotADirectoryError):
            functions.add_time_of_creation_2('nonexistent_folder')
        os.mkdir('test_folder_7')
        os.chdir('test_folder_7')
        test_file_10 = open('10.txt', 'a+')
        test_file_10.close()
        test_file_11 = open('11.txt', 'a+')
        test_file_11.close()
        test_file_12 = open('12.txt', 'a+')
        test_file_12.close()
        os.mkdir('test_folder_8')
        os.chdir('test_folder_8')
        test_file_13 = open('13.txt', 'a+')
        test_file_13.close()
        os.chdir('..')
        os.chdir('..')
        date_of_creation = datetime.datetime.today().strftime("%Y-%m-%d")
        tf_10_dc = '10' + ' ' + date_of_creation + '.txt'
        tf_11_dc = '11' + ' ' + date_of_creation + '.txt'
        tf_12_dc = '12' + ' ' + date_of_creation + '.txt'
        functions.add_time_of_creation_2('test_folder_7')
        os.chdir('test_folder_7')
        self.assertTrue(os.path.isfile(tf_10_dc))
        self.assertTrue(os.path.isfile(tf_11_dc))
        self.assertTrue(os.path.isfile(tf_12_dc))
        os.chdir('test_folder_8')
        self.assertTrue(os.path.isfile('13.txt'))
        os.chdir('..')
        os.chdir('..')
        shutil.rmtree('test_folder_7')

    def test_feature_5c(self):
        """
        Тестирует add_time_of_creation_3 функцию на следующее:
        - на появление ошибки, если передано название папки, которой не существует;
        - на добавление даты создания файла в названия всех файлов,
        которые находятся в указанной папке, включая все файлы во вложенных папках.
        """
        with self.assertRaises(NotADirectoryError):
            functions.add_time_of_creation_3('nonexistent_folder')
        os.mkdir('test_folder_9')
        os.chdir('test_folder_9')
        test_file_14 = open('14.txt', 'a+')
        test_file_14.close()
        os.mkdir('test_folder_10')
        os.chdir('test_folder_10')
        test_file_15 = open('15.txt', 'a+')
        test_file_15.close()
        os.mkdir('test_folder_11')
        os.chdir('test_folder_11')
        test_file_16 = open('16.txt', 'a+')
        test_file_16.close()
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        date_of_creation = datetime.datetime.today().strftime("%Y-%m-%d")
        tf_14_dc = '14' + ' ' + date_of_creation + '.txt'
        tf_15_dc = '15' + ' ' + date_of_creation + '.txt'
        tf_16_dc = '16' + ' ' + date_of_creation + '.txt'
        functions.add_time_of_creation_3('test_folder_9')
        os.chdir('test_folder_9')
        self.assertTrue(os.path.isfile(tf_14_dc))
        os.chdir('test_folder_10')
        self.assertTrue(os.path.isfile(tf_15_dc))
        os.chdir('test_folder_11')
        self.assertTrue(os.path.isfile(tf_16_dc))
        os.chdir('..')
        os.chdir('..')
        os.chdir('..')
        shutil.rmtree('test_folder_9')
