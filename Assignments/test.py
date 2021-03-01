from typing import List


def even(start, n) -> List:
    flag: bool = True
    res: List = []
    while(flag):
        if start % 2 == 0:
            res.append(start)
        if len(res) == n:
            flag = False
        start += 2
    return res


def main() -> None:
    test = even(2, 4)
    print(test)


if __name__ == '__main__':
    main()
