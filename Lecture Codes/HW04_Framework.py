# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:53:34 2016

@author: jrr
"""


import random
import unittest
from typing import Any, List, Optional, Sequence, Iterator

# PART 1

def count_vowels(s: str) -> int:
    ''' return the number of vowels in the string s '''
    # TODO: implement me
    return 0
        
# PART 2
    
def find_last(target: Any, seq: Sequence[Any]) -> Optional[int]:
    ''' return the offset from 0 of the last occurrence of target in seq '''
    # TODO: implement me
    return None
  
# PART 3 is Fraction.simplify()

# PART 4
def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """ emulate the behavior of Python's built in enumerate() function.
        For each call, return a tuple with the offset from 0 and the next item
    """
    # TODO: implement me
    yield 0, None  # replace with implementation


# PART 5

def generator(min_val: int, max_val: int) -> Iterator[int]:
    """ yield an infinite number of integers """
    # TODO: implement me
    yield 0  # replace with implementation

def find_target(target: int, min_val: int=0, max_val: int=10, max_attempts: int=100) -> Optional[int]:
    """ Count the number of random values read before finding target """
    # TODO: implement me
        
    return None