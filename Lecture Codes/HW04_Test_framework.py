# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:53:34 2016

@author: jrr
"""


import random
import unittest
from typing import Iterator, List, Tuple
from HW04_First_Last import count_vowels, count_vowels_pythonic, find_last, find_last_reverse
from HW04_First_Last import my_enumerate, my_enumerate_sarita, my_enumerate_yinghui, find_target, generator
# PART 1
    
class CountVowelsTest(unittest.TestCase):
    def test_count_vowels(self):
        """ testing count vowels """
        
# PART 2
    
class FindLastTest(unittest.TestCase):
    def test_find_last(self) -> None:
        """ testing find_last """
    
# PART 3 is Fraction.simplify()

# PART 4

class EnumerateTest(unittest.TestCase):
    def test_enumerate_list(self) -> None:
        """ test my_enumerate by storing the results in a list """
        
# PART 5
  
class FindTargetTest(unittest.TestCase):
    def test_random_generator(self) -> None:
        """ verify RandomGenerator correct """
        
    def test_find_target(self) -> None:
        """ verify find_target works for special case """
        
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)