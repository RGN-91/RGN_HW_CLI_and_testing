import unittest
import functions
import argparse

class TestFaF(unittest.TestCase):
    def test_feature_1(self):
        with self.assertRaises(FileNotFoundError):
            functions.copy_file()