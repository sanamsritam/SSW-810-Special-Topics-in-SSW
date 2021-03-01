from typing import DefaultDict, Dict


def offsets(seq) -> Dict:
    result = DefaultDict(list)
    for offset, item in enumerate(seq):
        result[item].append(offset)
    return result


def main() -> None:
    test: Dict = offsets("mississippi")
    print(test)


if __name__ == '__main__':
    main()
