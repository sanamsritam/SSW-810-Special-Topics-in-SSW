"""
Author: Sanam Jena
CWID:10454295
Date: 10 October 2020
Objective: string methods, slices, working with files, and automated testing
"""
from typing import Iterator


class HomeWork05:
    """In this class we will be creating the function which we will be using to complete the requirements of HW05.
    """

    def reverse(self, s: str) -> str:
        """In this function we are reversing a string. This method has the second least time complexity after slice. Using code after approval from Prof Raz.

        Args:
            s (str): original string

        Returns:
            str: reversed string
        """
        s = "".join(reversed(s))
        return s

    def substring(self, target: str, s: str) -> int:
        """In this function, we will be returning the offset/index at which the target is found in the input string.

        Args:
            target (str)
            s (str)

        Returns:
            int: index/position
        """
        if not isinstance(target, str):
            raise ValueError("Input must be of type string")
        if len(target) < 1:
            return 0
        if len(s) < 1:
            return -1
        for i in range(len(s)):
            if(s[i:i+len(target)] == target):
                return i
        return -1

    def find_second(self, target: str, string: str) -> int:
        """In this function, we will be returning the offset/index of the second occurence of target in string.

        Args:
            target (str): the thing we are looking for
            string (str): the original strring in which we need to search for

        Returns:
            int: index/position
        """
        start: int = self.substring(target, string)
        result: int = string.find(target, start+1)
        return result

    def get_lines(self, path: str) -> Iterator[str]:
        """In this function, we will be opening a file, reading and returning one line from the file at a time.
        In order to finish this function, I have discussed the idea with Rajat Verma.

        Args:
            path (str)

        Yields:
            Iterator[str]
        """
        try:
            fp = open(path, 'r')
        except FileNotFoundError:
            print(f"Cant open {path}")
        else:
            with fp:
                for line in fp:
                    # https://learning.oreilly.com/library/view/python-programming-with/0201616165/0201616165_ch10lev1sec5.html
                    line = line.rstrip('\n')
                    while line.endswith('\\'):
                        slashpointer: int = line.find('\\')
                        # In this line, we are adding spaces manually
                        line = line[:slashpointer]+" "
                        line = line[:-1] + fp.readline().strip('\n')
                    # In this line we are removing all the lines that begin with #
                    line = line.split('#', 1)[0].strip('\n')
                    if line:
                        yield line
                    else:
                        continue

    def __init__(self, s: str) -> None:
        if not isinstance(s, str):  # If the input is not of type 'string', raise ValueError
            raise ValueError("Input must be of type string")
        """if len(s) < 1:  # If string is empty, raise ValueError
            raise ValueError("Input can not be an empty string!")"""
        self.s: str = s


def main() -> None:
    file_name = 'Users/sanam/Documents/Desk/SSW 810 B/Assignments/test1.txt'
    test: HomeWork05 = HomeWork05("")
    for line in test.get_lines(file_name):
        print(line)


if __name__ == '__main__':
    main()


# 1)
s = "hello"
for i in range(len(s)):
    print(s[i:i+1])
# 2)
s = "hello"
for i in s:
    print(i)
# 3)
s = "hello"
i: int = 0
while i < len(s):
    print(s[i:i+1])
    i = i+1
