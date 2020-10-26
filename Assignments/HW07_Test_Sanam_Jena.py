"""
Author: Sanam Jena
CWID:10454295
Date: 21 October 2020
Objective: To write the test class in order to test HW07
"""
from typing import List, Tuple
import unittest
from HW07_Sanam_Jena import HomeWork07


class HomeWork07Test(unittest.TestCase):
    def test_anagrams_list(self) -> None:
        """In this function, we will be testing the anagrams_lst function from HomeWork07 class.
        """
        test: HomeWork07 = HomeWork07()
        self.assertEquals(test.anagrams_lst("Dirtyroom", "Dormitory"), True)
        self.assertEquals(test.anagrams_lst("Cinema", "Iceman"), True)
        self.assertEquals(test.anagrams_lst("Sanam", "Manas"), True)
        self.assertEquals(test.anagrams_lst("Sanam", "Jena"), False)
        self.assertEquals(test.anagrams_lst("", ""), True)
        self.assertEquals(test.anagrams_lst("123", "321"), True)
        with self.assertRaises(ValueError, msg="Input str1 must be of type str"):
            test.anagrams_lst(9, "Dormitory")
        with self.assertRaises(ValueError, msg="Input str2 must be of type str"):
            test.anagrams_lst("Dormitory", 9)

    def test_anagrams_defaultdict(self) -> None:
        """In this function, we will be testing the anagrams_dd function from HomeWork07 class.
        """
        test: HomeWork07 = HomeWork07()
        self.assertEquals(test.anagrams_dd("Dirtyroom", "Dormitory"), True)
        self.assertEquals(test.anagrams_dd("Cinema", "Iceman"), True)
        self.assertEquals(test.anagrams_dd("Sanam", "Manas"), True)
        self.assertEquals(test.anagrams_dd("Sanam", "Jena"), False)
        self.assertEquals(test.anagrams_dd("", ""), True)
        self.assertEquals(test.anagrams_dd("123", "321"), True)
        with self.assertRaises(ValueError, msg="Input str1 must be of type str"):
            test.anagrams_dd(9, "Dormitory")
        with self.assertRaises(ValueError, msg="Input str2 must be of type str"):
            test.anagrams_dd("Dormitory", 9)

    def test_anagrams_cntr(self) -> None:
        """In this function, we will be testing the anagrams_cntr function from HomeWork07 class.
        """
        test: HomeWork07 = HomeWork07()
        self.assertEquals(test.anagrams_cntr("Dirtyroom", "Dormitory"), True)
        self.assertEquals(test.anagrams_cntr("Cinema", "Iceman"), True)
        self.assertEquals(test.anagrams_cntr("Sanam", "Manas"), True)
        self.assertEquals(test.anagrams_cntr("Sanam", "Jena"), False)
        self.assertEquals(test.anagrams_cntr("", ""), True)
        self.assertEquals(test.anagrams_cntr("123", "321"), True)
        with self.assertRaises(ValueError, msg="Input str1 must be of type str"):
            test.anagrams_cntr(9, "Dormitory")
        with self.assertRaises(ValueError, msg="Input str2 must be of type str"):
            test.anagrams_cntr("Dormitory", 9)

    def test_covers_alphabet(self) -> None:
        """In this function, we will be testing the covers_alphabet function from HomeWork07 class.
        """
        test: HomeWork07 = HomeWork07()
        self.assertEquals(test.covers_alphabet(
            "qwertyuiopasdfghjklzxcvbnm"), True)
        self.assertEquals(test.covers_alphabet(
            "We promptly judged antique ivory buckles for the next prize"), True)
        self.assertEquals(test.covers_alphabet("xyz"), False)
        with self.assertRaises(ValueError, msg="Input sentence must be of type str"):
            test.covers_alphabet(9)

    def test_web_analyzer(self) -> None:
        """In this function, we will be testing the web_analyzer function from HomeWork07 class.
        """
        test: HomeWork07 = HomeWork07()
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]

        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(test.web_analyzer(weblogs), summary)
        with self.assertRaises(ValueError, msg="Input weblogs must be of type List"):
            test.web_analyzer(9)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
