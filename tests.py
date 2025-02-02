import unittest
import functions
import pathlib
import os


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
