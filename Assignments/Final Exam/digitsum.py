from typing import List


def digit_sum(n: int) -> int:
    lst: List = []
    for digit in str(n):
        lst.append(int(digit))
    print(lst)
    return n


def main():
    print(digit_sum(123))


if __name__ == '__main__':
    main()
