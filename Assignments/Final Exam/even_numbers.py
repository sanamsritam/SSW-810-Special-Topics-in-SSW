def calcuate():
    total = 0
    for number in range(2, 72, 2):
        total = total + number
    return total


def main():
    print(calcuate())


if __name__ == '__main__':
    main()
