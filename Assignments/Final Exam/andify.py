"""
        Date: 06 December 2020
        Author: Rajat verma
"""

"""    for x in sorted(test):
        if x == len(test):
            result += "and "+x

        result += ", "+x
"""




from typing import List
def andify(test: List) -> str:

    result: str = ""
    test1: List = sorted(test)
    res1: List = []

    for i in range(0, len(test)):
        if i == (len(test)-1):
            res1.append("and ")
            res1.append(str(test1[i]))
            break
        res1.append(str(test1[i]))
        res1.append(", ")

    for x in res1:
        result += x
    result = result[:-1]
    print("Result = ")
    print(result)
    return result


def main() -> None:
    print(andify(['tigers', 'dogs', 'cats', 'monkeys']))


if __name__ == '__main__':
    main()
