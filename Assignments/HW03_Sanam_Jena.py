"""
Author: Sanam Jena
CWID:10454295
Date: 25 Sept 2020
Objective: A simple fraction calculator in which a fraction is created based on input of the user and mathematical operations are performed of users's choice.
1. Rename the previous function names and remove print statements
2. Added simplify method inside class Fraction to simplify the fraction as part of HW04. (Updated 02 October 2020)
3. Added GCD(Greatest Common Divisor) method to calculate the GCD inorder to help in simplifying the fraction as part of HW04. (Updated 02 October 2020)
"""


class Fraction:
    """
    With the help of this calss, we can Add, Subtract, Multiply, __truediv__ & Compare
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

    def __add__(self, other: "Fraction") -> "Fraction":
        """
        In this function, we will be taking 2 fractions, adding them up and returning the final result as a Fraction.
        """
        resnum: float = (self.numerator * other.denominator) + \
            (self.denominator * other.numerator)
        resden: float = self.denominator * other.denominator
        return Fraction(resnum, resden)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """
        In this function, we will be taking two fractions and subtracting the second fraction from the first fraction and returning the final result as a Fraction.
        """
        resnum: float = (self.numerator*other.denominator) - \
            (self.denominator*other.numerator)
        resden: float = self.denominator * other.denominator
        return Fraction(resnum, resden)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """
        In this function, we will be taking two fractions as input and multiply both of them and return the final result as a Fraction.
        """
        resnum: float = self.numerator * other.numerator
        resden: float = self.denominator * other.denominator
        return Fraction(resnum, resden)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """
        In this function, we will be taking two fractions as input and perform the __truediv__ operation and return the final result as a Fraction.
        """
        resnum: float = self.numerator * other.denominator
        resden: float = self.denominator * other.numerator
        return Fraction(resnum, resden)

    def __eq__(self, other: "Fraction") -> bool:
        """
        In this function, we will take two fractions as input and compare if the both them are equal or not and return the final result as a Fraction.
        """
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ne__(self, other: "Fraction") -> bool:
        """[In this function, we will take two fractions as input and compare if the both them are not equal and return the final result as a Fraction.]

        Args:
            other (Fraction)

        Returns:
            bool
        """
        return self.numerator * other.denominator != self.denominator * other.numerator

    def __lt__(self, other: "Fraction") -> bool:
        """[In this function, we will take two fractions as input and compare if self is less than other and return the final result as a Fraction.]

        Args:
            other (Fraction):

        Returns:
            bool:
        """
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __le__(self, other: "Fraction") -> bool:
        """[In this function, we will take two fractions as input and compare if self is less than or equal to other and return the final result as a Fraction.]

        Args:
            other (Fraction):

        Returns:
            bool:
        """
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __gt__(self, other: "Fraction") -> bool:
        """[In this function, we will take two fractions as input and compare if self is greater than other and return the final result as a Fraction.]

        Args:
            other (Fraction):

        Returns:
            bool:
        """
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __ge__(self, other: "Fraction") -> bool:
        """[In this function, we will take two fractions as input and compare if self is greater than or equal to other and return the final result as a Fraction.]

        Args:
            other (Fraction)

        Returns:
            bool
        """
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def gcd(self, numerator: int, denominator: int) -> int:
        """[In this function, we are calculating the GCD(Greatest Common Divisor) otherwise known as HCF(Highest Common Factor) and returning the same to be used by
        simplify function in order to simplify the fraction.]

        Args:
            numerator (int)
            denominator (int)

        Returns:
            hcf (int)

        Explanation:
            Here we will be looping until Denominator becomes zero. The statement numerator, Denominator = Denominator, numerator % Denominator does swapping of values,
            in each iteration we replace the value of denominator in numerator and the remainder (numerator % denominator) in denominator simultaneously.
            When denominator becomes zero, we have GCD in numerator. This method of calculation of GCD is known as Euclidean Algorithm the time complexity of this is comparatively less.
            Using this uppon approval from Prof. Raz.
        """
        while(denominator):
            numerator, denominator = denominator, numerator % denominator
        return numerator

    def simplify(self) -> "Fraction":
        """[In this function, we are performing the actual simplification of the fraction by using the value of GCD.]
        """
        if((self.numerator > 0) and (self.denominator < 0)):
            x = self.gcd(abs(self.numerator), abs(self.denominator))
            numerator1: float = -(self.numerator/x)
            denominator1: float = -(self.denominator/x)
            return Fraction(numerator1, denominator1)
        elif((self.numerator < 0) and (self.denominator < 0)):
            x = self.gcd(abs(self.numerator), abs(self.denominator))
            numerator1: float = -(self.numerator/x)
            denominator1: float = -(self.denominator/x)
            return Fraction(numerator1, denominator1)
        else:
            x = self.gcd(abs(self.numerator), abs(self.denominator))
            numerator1: float = self.numerator/x
            denominator1: float = self.denominator/x
            return Fraction(numerator1, denominator1)

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
        input1: str = input(prompt)
        try:
            return float(input1)

        except ValueError as e:
            raise ValueError(
                "Error: '{input1}' is not a valid number. Please enter only numeric values!")
            #print("Please enter only numeric Value, Try again!")
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
        except ZeroDivisionError as e:
            raise ZeroDivisionError(
                "Error: '{Denominator}' is zero(0). The denominator of a fraction cannot be Zero!!")
        else:
            return Fraction(Numerator, Denominator)


def compute(f1: "Fraction", operator: str, f2: "Fraction") -> None:
    """
    In this function, we will call the appropriate operation function based on the user's input choide and print the final result post computation.
    """
    result: "Fraction"

    if operator == "+":
        #print(f'{f1.numerator} / {f1.denominator} + {f2.numerator} / {f2.denominator} = {str(f1.__add__(f2))}')
        result = f1 + f2
    elif operator == "-":
        #print(f'{f1.numerator} / {f1.denominator} - {f2.numerator} / {f2.denominator} = {str(f1.__sub__(f2))}')
        result = f1 - f2
    elif operator == "*":
        #print(f'{f1.numerator} / {f1.denominator} * {f2.numerator} / {f2.denominator} = {str(f1.__mul__(f2))}')
        result = f1 * f2
    elif operator == "/":
        #print(f'{f1.numerator} / {f1.denominator} / {f2.numerator} / {f2.denominator} = {str(f1.__truediv__(f2))}')
        result = f1 / f2
    elif operator == "==":
        #print(f'{f1.numerator} / {f1.denominator} == {f2.numerator} / {f2.denominator} = {str(f1.__eq__(f2))}')
        result = f1 == f2
    elif operator == '!=':
        result = f1 != f2
    elif operator == '>':
        result = f1 > f2
    elif operator == '>=':
        result = f1 >= f2
    elif operator == '<':
        result = f1 < f2
    elif operator == '<=':
        result = f1 <= f2
    print(f"{f1} {operator} {f2} = {result}")


def check_operator(operator: str) -> bool:
    """
    This function checks for the valid input of the operators and returns a boolean value.
    """
    oprs = ["+", "-", "*", "/", "==", "!=", "<", "<=", ">", ">="]
    if(operator not in oprs):
        return True
    else:
        return False


def main() -> None:
    """
    This is the main method otherwise the heart of the program, it calls various functions based on the requirement in order to run the program
    """
    #print("Welcome to the fraction calculator!")
    #print("Fraction 1")
    f1: Fraction = get_Fraction()
    opr = input("Operation (+, -, *, /, ==, !=, <, <=, >, >=):")
    loop: bool = check_operator(opr)
    while loop:
        if loop:
            #print("Invalid input for operator, Try again!")
            opr = input(
                "Invalid input for operator. Operation (+, -, *, /, ==, !=, <, <=, >, >=):")
            loop: bool = check_operator(opr)
        else:
            loop: bool = False
            pass
    #print("Fraction 2")
    other: Fraction = get_Fraction()
    compute(f1, opr, other)


"""def test_suite() -> None:

    # This class tests the custom test cases as asked in the assignment

    print("***TEST SUITE***")
    f12: Fraction = Fraction(1, 2)
    f32: Fraction = Fraction(3, 2)
    f34: Fraction = Fraction(3, 4)
    f44: Fraction = Fraction(4, 4)
    f68: Fraction = Fraction(6, 8)
    f128: Fraction = Fraction(12, 8)
    f912: Fraction = Fraction(9, 12)

    print(f"{f12} + {f12} = {f12.__add__(f12)} [4/4]")
    print(f"{f44} - {f12} = {f44.__sub__(f12)} [4/8]")
    print(f"{f12} + {f44} = {f12.__add__(f44)} [12/8]")
    print(f"{f68} * {f912} = {f68.__mul__(f912)} [54/96]")
    print(f"{f34} / {f12} = {f34.__truediv__(f12)} [6/4]")
    print(f"{f128} == {f32} is {f128.__eq__(f32)} [True]")
    print(f"{f12} + {f34} = {f12.__add__(f12)} [10/8]")

    # include a test with three operands
    print(f"{f12} + {f34} + {f44} = {f12.__add__(f34).__add__(f44)} [72/32]")
"""

if __name__ == '__main__':
    main()
    # test_suite()
