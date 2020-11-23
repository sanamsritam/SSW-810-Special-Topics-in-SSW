"""
Author: Sanam Jena
CWID:10454295
Date: 17 Sept 2020
Objective: A simple fraction calculator in which a fraction is created based on input of the user and mathematical operations are performed of users's choice
"""


class Fraction:
    """
    With the help of this calss, we can Add, Subtract, Multiply, Divide & Compare
    two Fractions with simple algorithms.
    """

    def __init__(self, numerator: float, denominator: float) -> None:
        """
        This method creates an instance of class Fraction and raises an exception if the Denominator of the Fraction is zero.
        """
        self.numerator: float = numerator
        if denominator == 0:
            raise ValueError(
                "The denominator of a fraction cannot be ZERO, Try Again!")
        self.denominator: float = denominator

    def plus(self, other: "Fraction") -> "Fraction":
        """
        In this function, we will be taking 2 fractions, adding them up and returning the final result as a Fraction.
        """
        resnum: float = (self.numerator * other.denominator) + \
            (self.denominator * other.numerator)
        resden: float = self.denominator * other.denominator
        return Fraction(resnum, resden)

    def minus(self, other: "Fraction") -> "Fraction":
        """
        In this function, we will be taking two fractions and subtracting the second fraction from the first fraction and returning the final result as a Fraction.
        """
        resnum: float = (self.numerator * other.denominator) - \
            (self.denominator * other.numerator)
        resden: float = self.denominator * other.denominator
        return Fraction(resnum, resden)

    def times(self, other: "Fraction") -> "Fraction":
        """
        In this function, we will be taking two fractions as input and multiply both of them and return the final result as a Fraction.
        """
        resnum: float = self.numerator * other.numerator
        resden: float = self.denominator * other.denominator
        return Fraction(resnum, resden)

    def divide(self, other: "Fraction") -> "Fraction":
        """
        In this function, we will be taking two fractions as input and perform the divide operation and return the final result as a Fraction.
        """
        resnum: float = self.numerator * other.denominator
        resden: float = self.denominator * other.numerator
        return Fraction(resnum, resden)

    def equal(self, other: "Fraction") -> bool:
        """
        In this function, we will take two fractions as input and compare if the both them are equal or not and return the final result as a Fraction.
        """
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __str__(self) -> str:
        """
        This function prints the fraction.
        """
        return str(self.numerator) + "/" + str(self.denominator)


def get_number(prompt: str) -> float:
    """
    In this function, we take the input of each part of the Fraction (Numerator & Denominator), validate the same and return the input received from the User.
    """
    loop: bool = True
    while loop:
        try:
            input1: str = input(prompt)
            return float(input1)

        except ValueError as e:
            print("Please enter only numeric Value, Try again!")
            continue


def get_Fraction() -> "Fraction":
    """
    In this function, we create the fraction by assigning the values to the numerator and denominator and return the instance of the Fraction that we have created.
    """
    Numerator: float = float(get_number("Enter the value for Numerator:"))
    while True:
        Denominator: float = float(get_number(
            "Enter the value for Denominator:"))
        try:
            Fraction(Numerator, Denominator)
        except ValueError:
            print("The denominator of a fraction cannot be ZERO, Try Again!")
        except BaseException:
            print(f"OOPs Something went wrong: {BaseException}, Try Again!")
        else:
            return Fraction(Numerator, Denominator)


def compute(f1: "Fraction", operator: str, other: "Fraction") -> None:
    """
    In this function, we will call the appropriate operation function based on the user's input choide and print the final result post computation.
    """
    if operator == "+":
        print(f'{f1.numerator} / {f1.denominator} + {other.numerator} / {other.denominator} = {str(f1.plus(other))}')
    elif operator == "-":
        print(f'{f1.numerator} / {f1.denominator} - {other.numerator} / {other.denominator} = {str(f1.minus(other))}')
    elif operator == "*":
        print(f'{f1.numerator} / {f1.denominator} * {other.numerator} / {other.denominator} = {str(f1.times(other))}')
    elif operator == "/":
        print(f'{f1.numerator} / {f1.denominator} / {other.numerator} / {other.denominator} = {str(f1.divide(other))}')
    elif operator == "==":
        print(f'{f1.numerator} / {f1.denominator} == {other.numerator} / {other.denominator} = {str(f1.equal(other))}')


def check_operator(operator: str) -> bool:
    """
    This function checks for the valid input of the operators and returns a boolean value.
    """
    oprs = ["+", "-", "*", "/", "=="]
    if(operator not in oprs):
        return True
    else:
        return False


def main() -> None:
    """
    This is the main method otherwise the heart of the program, it calls various functions based on the requirement in order to run the program
    """
    print("Welcome to the fraction calculator!")
    print("Fraction 1")
    f1: Fraction = get_Fraction()
    opr = input("Operation (+, -, *, /, ==):")
    loop: bool = check_operator(opr)
    while loop:
        if loop:
            print("Invalid input for operator, Try again!")
            opr = input("Operation (+, -, *, /, ==):")
            loop: bool = check_operator(opr)
        else:
            pass
    print("Fraction 2")
    other: Fraction = get_Fraction()
    compute(f1, opr, other)


def test_suite() -> None:
    """
    This class tests the custom test cases as asked in the assignment
    """
    print("***TEST SUITE***")
    f12: Fraction = Fraction(1, 2)
    f32: Fraction = Fraction(3, 2)
    f34: Fraction = Fraction(3, 4)
    f44: Fraction = Fraction(4, 4)
    f68: Fraction = Fraction(6, 8)
    f128: Fraction = Fraction(12, 8)
    f912: Fraction = Fraction(9, 12)

    print(f"{f12} + {f12} = {f12.plus(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.minus(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.plus(f44)} [12/8]")
    print(f"{f68} * {f912} = {f68.times(f912)} [54/96]")
    print(f"{f34} / {f12} = {f34.divide(f12)} [6/4]")
    print(f"{f128} == {f32} is {f128.equal(f32)} [True]")
    print(f"{f12} + {f34} = {f12.plus(f12)} [10/8]")

    # include a test with three operands
    print(f"{f12} + {f34} + {f44} = {f12.plus(f34).plus(f44)} [72/32]")


if __name__ == '__main__':
    main()
    test_suite()
