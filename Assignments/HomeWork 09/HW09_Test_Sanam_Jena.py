"""
Author: Sanam Jena
CWID:10454295
Date: 13 December 2020
Objective: To write the test class in order to test HW10
"""

import unittest
from HW09_Sanam_Jena import Repository


class HW09TestCase(unittest.TestCase):
    """
    class to test the HW10 assignment
    """

    def test_students(self):
        """
        to test student
        """
        self.r: Repository = Repository(
            "C:\\Users\\sanam\\Documents\\Desk\\SSW 810 B\\Assignments\\HomeWork 09")

        expected = {'10103': ['10103', 'Baldwin, C',
                              ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10115': ['10115', 'Wyatt, X',
                              ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
                    '10172': ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']],
                    '10175': ['10175', 'Erickson, D',
                              ['SSW 564', 'SSW 567', 'SSW 687']],
                    '10183': ['10183', 'Chapman, O', ['SSW 689']],
                    '11399': ['11399', 'Cordova, I', ['SSW 540']],
                    '11461': ['11461', 'Wright, U',
                              ['SYS 611', 'SYS 750', 'SYS 800']],
                    '11658': ['11658', 'Kelly, P', ['SSW 540']],
                    '11714': ['11714', 'Morton, A', ['SYS 611', 'SYS 645']],
                    '11788': ['11788', 'Fuller, E', ['SSW 540']]}

        result = {cwid: student.info()
                  for cwid, student in self.r._students.items()}
        self.assertEqual(expected, result)

    def test_instructor(self) -> None:
        """
        To test instructor
        """
        self.r: Repository = Repository(
            "C:\\Users\\sanam\\Documents\\Desk\\SSW 810 B\\Assignments\\HomeWork 09")
        expected = {('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
                    ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
                    ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
                    ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
                    ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
                    ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
                    ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)}
        result = {tuple(
            detail) for instructor in self.r._instructors.values(
        ) for detail in instructor.info()}
        self.assertEqual(expected, result)

    def test_filenotfound(self) -> None:
        """
        Function to test if file is not found
        """
        self.r: Repository = Repository(
            "C:\\Users\\sanam\\Documents\\Desk\\SSW 810 B\\Assignments\\Wrong Input")
        with self.assertRaises(FileNotFoundError):
            Repository("Filenotfound")

    def test_valueerror(self) -> None:
        """
        Function to test if a value is missing
        """

        with self.assertRaises(ValueError):
            Repository(
                "C:\\Users\\sanam\\Documents\\Desk\\SSW 810 B\\Assignments\\HomeWork 09\\Test")

    def test_wrong_noOf_fields(self) -> None:
        """
        Function to test if a field is extra
        """

        with self.assertRaises(ValueError):
            Repository(
                "C:\\Users\\sanam\\Documents\\Desk\\SSW 810 B\\Assignments\\HomeWork 09\\Test")

    def test_no_record(self) -> None:
        """
        Function to test if a record in grade is not present in student/instructor
        """
        with self.assertRaises(KeyError):
            Repository(
                "C:\\Users\\sanam\\Documents\\Desk\\SSW 810 B\\Assignments\\HomeWork 09\\Test")

    def test_duplicate_values(self) -> None:
        """
        Function to test for duplicate records of students/professors
        """
        with self.assertRaises(KeyError):
            Repository(
                "C:\\Users\\sanam\\Documents\\Desk\\SSW 810 B\\Assignments\\HomeWork 09\\Test")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
