"""
Author: Sanam Jena
CWID:10454295
Date: 10 October 2020
Objective: To write test class for HW05
"""
import unittest
from HW05_Sanam_Jena import HomeWork05


class HomeWork05Test(unittest.TestCase):
    """Testing the Reverse function"""

    def test_reverse(self) -> None:
        """In this function, we will be testing the reverse function
        """
        test: HomeWork05 = HomeWork05("Sanam")
        self.assertEqual(test.s, "Sanam")  # Checking if init works
        # Checking if reverse works
        self.assertEqual(test.reverse(test.s), "manaS")
        test1: HomeWork05 = HomeWork05("madam")
        # checking for a palindrome
        self.assertEqual(test1.reverse(test1.s), "madam")
        test2: HomeWork05 = HomeWork05("x")
        self.assertEqual(test2.reverse(test2.s), "x")
        test3: HomeWork05 = HomeWork05("abc")
        self.assertNotEqual(test3.reverse(test3.s), "abc")
        test4: HomeWork05 = HomeWork05(" ")
        self.assertEqual(test4.reverse(test4.s), " ")
        with self.assertRaises(ValueError, msg="Input must be of type string"):
            test5: HomeWork05 = HomeWork05(55)

    def test_substring(self) -> None:
        """In this function, we will be testing the substring function
        """
        test: HomeWork05 = HomeWork05("Sanam")
        self.assertEqual(test.substring("San", test.s), 0)
        self.assertEqual(test.substring("an", test.s), 1)
        self.assertEqual(test.substring("Je", test.s), -1)
        self.assertEqual(test.substring("Je", ""), -1)
        self.assertEqual(test.substring("", test.s), 0)
        self.assertEqual(test.substring("", ""), 0)

    def test_find_second(self) -> None:
        """In this function we will be testing the find_second function.
        """
        test: HomeWork05 = HomeWork05("Sanam")
        self.assertEqual(test.find_second("a", test.s), 3)
        test1: HomeWork05 = HomeWork05("Mississippi")
        self.assertEqual(test1.find_second("iss", test1.s), 4)
        self.assertEqual(test1.find_second("xyz", test1.s), -1)

    def test_get_lines(self) -> None:
        """In this function, we will be testing the get_lines function.
        """
        test: HomeWork05 = HomeWork05("")
        file_name: str = '/Users/sanam/Documents/Desk/SSW 810 B/Assignments/test1.txt'
        expect: List[str] = ['<line0>', '<line1>', '<line2>',
                             '<line3.1 line3.2 line3.3>', '<line4.1 line4.2>', '<line5>', '<line6>']
        result: List[str] = list(test.get_lines(file_name))
        self.assertEqual(result, expect)

        # Testing for empty file
        file_name_2: str = '/Users/sanam/Documents/Desk/SSW 810 B/Assignments/test2.txt'
        expect1: List[str] = []
        result1: List[str] = list(test.get_lines(file_name_2))
        self.assertEqual(result1, expect1)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
