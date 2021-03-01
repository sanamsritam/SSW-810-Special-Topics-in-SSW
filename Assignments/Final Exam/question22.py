"""
    Date: 06 December 2020
    Author: Sanam Sritam Jena
"""


class Weight:
    def __init__(self, pound: int, ounce: int) -> None:
        self.pound: int = pound + ounce//16
        self.ounce: int = ounce % 16
        self.label: str = f"{self.pound} pounds and {self.ounce} ounce"

    def __str__(self) -> str:
        """ return a String to display Weights """
        return f"{self.label}"

    def __add__(self, other: "Weight") -> "Weight":
        """ Add two Weights using simplest approach.
            Calculate new numerator and denominator and return new Weight
        """
        pound: int = (self.pound + other.pound) + \
            (self.ounce + other.ounce)//16
        ounce: int = (self.ounce + other.ounce) % 16

        result: Weight = Weight(pound, ounce)
        return result


def main() -> None:
    f1: Weight = Weight(5, 16)
    f2: Weight = Weight(5, 15)
    print(f1+f2)


if __name__ == '__main__':
    main()
