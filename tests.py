import unittest
import functions
import pathlib
import os
import shutil
import contextlib
import io


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