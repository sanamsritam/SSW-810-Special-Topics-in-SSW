"""
    Date: 06 December 2020
    Author: Sanam Sritam Jena
"""
from typing import Iterator


def up_down(n: int) -> Iterator[int]:
    """Count up to n and go back to zero

    Args:
        n (int): [description]

    Yields:
        Iterator[int]: [description]
    """
    yield from range(n)
    yield from range(n, -1, -1)


def main() -> None:
    for i in up_down(5):
        print(i)


if __name__ == '__main__':
    main()
