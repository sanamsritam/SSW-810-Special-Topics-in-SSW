"""
    Date: 06 December 2020
    Author: Sanam Sritam Jena
"""


def lower_case(string: str):
    string = string.split()
    lst = [x.lower() for x in string]
    str1 = " "
    print(str1.join(lst))
    return str1


def main():
    print(lower_case("STOP YELLING!"))


if __name__ == '__main__':
    main()
