"""
    Date: 06 December 2020
    Author: Sanam Sritam Jena
"""


def remove_spaces(input: str) -> str:
    """
    remove space from string
    """
    result: str = input.replace(" ", "")
    return result


def main() -> None:
    """ Main Function """
    string = "this has several spaces"
    print(remove_spaces(string))
    print("original ", string)


if __name__ == '__main__':
    main()
