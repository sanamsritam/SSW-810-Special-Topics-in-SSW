"""
    Date: 06 December 2020
    Author: Sanam Sritam Jena
"""
from typing import List


def dup(my_list: List) -> List:
    output = [item for item in my_list]
    return output


def main() -> None:
    """ Main Function """
    print(dup([1, 2, 3]))


if __name__ == '__main__':
    main()
