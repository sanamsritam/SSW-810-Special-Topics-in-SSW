"""
Author: Sanam Jena
CWID:10454295
Date: 08 November 2020
Objective: In this assignment is to work on datetime,files & prettytable
"""

from typing import Tuple, Iterator, List, IO, Dict
from datetime import timedelta, datetime
from prettytable import PrettyTable
import os


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """In this function, we will be answering the following questions:
    1. What is the date three days after Feb 27, 2020?
    2. What is the date three days after Feb 27, 2019?
    3. How many days passed between Feb 1, 2019 and Sept 30, 2019?

    Returns:
        A tuple with three values in the following order:
        1. An instance of  class datetime representing the date three days
        after Feb 27, 2020.
        2. An instance of  class datetime representing the date three days
        after Feb 27, 2019.
        3. An int representing the number of days between Feb 1, 2019 and
        Sept 30, 2019
    """
    three_days_after_02272020: datetime = datetime(
        2020, 2, 27) + timedelta(days=3)
    three_days_after_02272019: datetime = datetime(
        2019, 2, 27) + timedelta(days=3)
    days_passed_02012019_09302019: int = (
        datetime(2019, 9, 30) - datetime(2019, 2, 1)).days

    return (
        three_days_after_02272020,
        three_days_after_02272019,
        days_passed_02012019_09302019)


def file_reader(path: str, fields: int, sep: str = ',',
                header: bool = False) -> Iterator[List[str]]:
    """In this function, we will implement a generator that will yield
    new line of a file on call of next

    Args:
        path (str): File Path
        fields (int): fields
        sep (str, optional): Separator. Defaults to ','.
        header (bool, optional): Defaults to False.

    Yields:
        Iterator[Tuple[str]]
    """
    try:
        fp: IO = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Cannot open file at {path} ")
    else:
        line_number: int = 0
        for line in fp:
            row: List[str] = line.strip().split(sep)
            line_number += 1
            if len(row) != fields:
                fp.close()
                raise ValueError(
                    f"File {path} at line {line_number} has  {len(row)} items, whereas the \
                    expected items where {fields} ")
            if header is False:
                yield row
            else:
                header = False


class FileAnalyzer:
    """given a directory name, searches that directory for Python files
    (i.e. files ending with .py). For each .py file in the directory, open
    each file and calculate a summary of the file including:
         1.the file name
         2.the total number of lines in the file
         3.the total number of characters in the file
         4.the number of Python functions (lines that begin with ‘def ’,
         including methods inside class definitions)
         5.the number of Python classes (lines that begin with ‘class ’)
    Discussed with Rajat Verma & Tehreem Tungekar
    """

    def __init__(self, directory: str) -> None:
        """ In this method, we are initializing the class
        """
        self.directory: str = directory  # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()  # summerize the python files data

    def analyze_files(self) -> None:
        """ In this method, we will be summarizing and storing the data
        into self.files_summary
        """
        path: str = self.directory
        direct: List[str] = os.listdir(path)
        for f in direct:
            if f.endswith('.py'):
                try:
                    fp = open(os.path.join(path, f), 'r')
                except FileNotFoundError:
                    raise FileNotFoundError(f"File {f} cannot be openend")
                else:
                    with fp:
                        character_count: int = 0
                        class_count: int = 0
                        function_count: int = 0
                        line_count: int = 0

                        for line in fp:
                            character_count += len(line)
                            line_count += 1

                            if line.strip().startswith('def '):
                                function_count += 1
                            if line.startswith('class '):
                                class_count += 1

                        self.files_summary[f] = {
                            'classes': class_count,
                            'functions': function_count,
                            'lines': line_count,
                            'characters': character_count
                        }

    def pretty_print(self) -> None:
        """In this function, we will print the summarized detail into
        a table using prettytable module
        """
        output: PrettyTable = PrettyTable()
        output.field_names = ['File Name', 'Classes',
                              'Functions', 'Lines', 'Characters']

        for i, j in self.files_summary.items():
            output.add_row([i, j['classes'], j['functions'],
                            j['lines'], j['characters']])

        print("\nSummary for ", self.directory)
        print(output)
