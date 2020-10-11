"""
Author: Sanam Jena
CWID:10454295
Date: 02 October 2020
Objective: practice iterating over lists, ranges, and strings using for and while loops
"""
from typing import Optional, Any, Iterator


def count_vowels(s: str) -> int:
    """In this function we will be counting the no of vowels present in the string

    Args:
        s (str): The string in which vowels have to be counted

    Returns:
        int: The no of vowels in the string
    """
    count: int = 0
    s1: str = s.lower()
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    for i in s1:
        if i in vowels:
            count += 1
    return count


def last_occurrence(target: any, sequence: [any]) -> Optional[int]:
    """In this function we will be returning the last occurence of the thing in the parameter provided to us

    Args:
        target (any)
        sequence ([type])

    Returns:
        Optional[int]
    """
    ans: Optional[int] = None
    for offset, i in enumerate(sequence):
        if i == target:
            ans = int(offset)
    return ans


def my_enumerate(seq) -> Iterator[Any]:
    """In this function, we will emulate the behavior of Python's built in enumerate() function.

    Args:
        seq ([type])

    Yields:
        Iterator[Any]
    """
    for offset in range(len(seq)):
        yield offset, seq[offset]
