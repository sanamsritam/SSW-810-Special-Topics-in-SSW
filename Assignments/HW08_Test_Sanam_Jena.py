"""
Author: Sanam Jena
CWID:10454295
Date: 08 November 2020
Objective: To write the test class in order to test HW08
"""

import unittest
from HW08_Sanam_Jena import date_arithmetic, file_reader, FileAnalyzer
from datetime import datetime
from prettytable import PrettyTable


class HW08Test(unittest.TestCase):
    """
    Class containing functions for test cases
    """

    def test_date_arithmatic(self):
        """
        In this function, we will test the date_arithmatic function
        """
        self.assertEqual(date_arithmetic(), (datetime(
            2020, 3, 1), datetime(2019, 3, 2), 241))
        self.assertNotEqual(date_arithmetic(), (datetime(
            2020, 3, 1), datetime(2019, 3, 2), 41))

    def test_file_reader(self) -> None:
        """
        In this function, we will the file_reader() function
        """
        result = [['123', 'Jin He', 'Computer Science'],
                  ['234', 'Nanda Koka', 'Software Engineering'],
                  ['345', 'Benji Cai', 'Software Engineering']]
        self.assertEqual(
            list(file_reader('./student_majors.txt', 3, '|', True)), result)
        self.assertNotEqual(
            list(file_reader('./student_majors.txt', 3, '|')), result)
        with self.assertRaises(ValueError):
            list(file_reader('./student_majors.txt', 4, '|', True))
        with self.assertRaises(FileNotFoundError):
            list(file_reader('abc.txt', 3, '|', True))

    def test_analyze_files(self) -> None:
        """
        In this function, we will the analyze_files function from FileAnalyzer
        class
        """
        test = FileAnalyzer('./HW08_Test')
        expected = {'HW08_Sanam_Jena.py':
                    {'classes': 1,
                     'functions': 5, 'lines': 140, 'characters': 5299}}
        self.assertEqual(test.files_summary, expected)
        with self.assertRaises(FileNotFoundError):
            FileAnalyzer(' ')

    def test_pretty_print(self) -> None:
        test2 = FileAnalyzer('./HW08_Test/')
        test2.pretty_print()


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
