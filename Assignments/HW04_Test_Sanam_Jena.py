"""
Author: Sanam Jena
CWID:10454295
Date: 02 October 2020
Objective: To write test class for HW4
"""
import unittest
from HW04_Sanam_Jena import count_vowels, last_occurrence, my_enumerate


class CountVowelTest(unittest.TestCase):
    def test1_count_vowels(self) -> None:
        """In this function, we are testing both true and false cases for the function count_vowels in HW04
        """
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("HEllO0"), 2)
        self.assertEqual(count_vowels("hmm"), 0)
        self.assertNotEqual(count_vowels("OKay"), 5)


class FindLastTest(unittest.TestCase):
    def test2_last_occurrence(self) -> None:
        """In this function, we are testing both true and false cases for the function last_occurrence in HW04
        """
        self.assertEqual(last_occurrence("l", "Hello"), 3)
        self.assertEqual(last_occurrence("1", "Hello"), None)
        self.assertEqual(last_occurrence(
            "Tiger", ["Lion", "Cheetah", "Snake", "Tiger", "Tiger"]), 4)
        self.assertEqual(last_occurrence(
            "s", "Hello"), None)
        self.assertEqual(last_occurrence('p', 'apple'), 2)
        self.assertNotEqual(last_occurrence("l", "hello"), 5)
        self.assertEqual(last_occurrence(
            "Hello", "l"), None)


class EnumerateTest(unittest.TestCase):
    def test3_enumerate(self) -> None:
        """In this function we will be testing out both true and false cases for the user defined enumerate function to function as a substitute to the built in function.
        my_enumerate function is present in HW04.
        """
        str1: str = list(my_enumerate("Sanam"))
        str2: str = list(enumerate("Sanam"))
        self.assertEqual(str1, str2)
        str3: str = list(my_enumerate("Sanam"))
        str4: str = list(enumerate("Sanam Jena"))
        self.assertNotEqual(str3, str4)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
