"""
    Date: 06 December 2020
    Author: Sanam Sritam Jena
"""


def sum_first_n_squares(num: int) -> int:
    """
    Sum of squares using list comprehension
    """
    if num < 1:
        raise ValueError("You have entered invalid value")
    return sum([int(num*num) for num in range(num+1)])


def main() -> None:
    """ Main Function """
    print(sum_first_n_squares(5))


if __name__ == '__main__':
    main()
