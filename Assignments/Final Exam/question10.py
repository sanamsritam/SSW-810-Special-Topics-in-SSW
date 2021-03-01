"""
    Date: 06 December 2020
    Author: Sanam Sritam Jena
"""


def my_range(start: int, limit: int, increment: int = 1) -> int:
    """
    my range generates numbers in between start and limit taking increment into consideration
    """
    i = start
    while i < limit:
        yield i
        i += increment


def main() -> None:
    print(list(my_range(2, 10, 2)))


if __name__ == '__main__':
    main()
