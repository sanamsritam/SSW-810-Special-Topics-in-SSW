"""
Author: Sanam Jena
CWID:10454295
Date: 21 October 2020
Objective: The goal of this assignment is to practice using list, tuple, dict, defaultdict, and set.
There are three parts to this assignment. None of the individual functions require much code,
but writing concise, elegant solutions may take a little thought.
"""

from typing import List, DefaultDict, Tuple
from collections import Counter, defaultdict
import string


class HomeWork07:
    """In this class we will writing all the functions required to complete HomeWork07
    """

    def __init__(self) -> None:
        return None

    def anagrams_lst(self, str1: str, str2: str) -> bool:
        """In this function we will be testing if both the parameters str1 & str2 are anagrams.
        this function returns true if both the strings are anagrams else returns false.

        Args:
            str1 (str)
            str2 (str)

        Returns:
            bool
        """
        if not isinstance(str1, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input str1 must be of type str")
        if not isinstance(str2, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input str2 must be of type str")
        return sorted(list(str1.lower())) == sorted(list(str2.lower()))

    def anagrams_dd(self, str1: str, str2: str) -> bool:
        """In this function, we will determine if two strings are anagrams using defaultdict

        Args:
            str1 (str)
            str2 (str)

        Returns:
            bool: returns true if both str1 and str2 are anagrams
        """
        if not isinstance(str1, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input str1 must be of type str")
        if not isinstance(str2, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input str2 must be of type str")
        dd: defaultdict[str, int] = defaultdict(int)
        for i in str1.lower():
            dd[i] += 1
        for i in str2.lower():
            dd[i] -= 1
        return not any(dd.values())

    def anagrams_cntr(self, str1: str, str2: str) -> bool:
        """In this function, we will determine if two strings are anagrams using only collections.Counters

        Args:
            str1 (str)
            str2 (str)

        Returns:
            bool: returns true if both str1 and str2 are anagrams
        """
        if not isinstance(str1, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input str1 must be of type str")
        if not isinstance(str2, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input str2 must be of type str")
        return Counter(str1.lower()) == Counter(str2.lower())

    def covers_alphabet(self, sentence: str) -> bool:
        """This function returns True if sentence includes at least one instance of every character in the 
        alphabet or False using only Python sets. Reffered to
        https://stackoverflow.com/questions/59726206/how-are-these-sets-equal-eli5 and discussed with Rajat Verma.

        Args:
            sentence (str)

        Returns:
            bool
        """
        if not isinstance(sentence, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input sentence must be of type str")
        return set(string.ascii_lowercase) <= set(sentence.lower())

    def web_analyzer(self, weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
        """This function creates a summary of the weblogs with each distinct site and a sorted list of names of
        distinct people who visited that site. Discussed with Prof Raz & Rajat Verma.

        Args:
            weblogs (List[Tuple[str, str]])

        Returns:
            List[Tuple[str, List[str]]]: each item in the list is a tuple with the employee name and the website he/she visited.
        """
        if not isinstance(weblogs, List):  # If the input is not of type 'List', raise ValueError
            raise ValueError("Input weblogs must be of type List")
        dd: DefaultDict[str, set[str]] = defaultdict(set)
        for names, webpage in weblogs:
            dd[webpage].add(names)
        return [(website, sorted(name)) for website, name in sorted(dd.items())]
