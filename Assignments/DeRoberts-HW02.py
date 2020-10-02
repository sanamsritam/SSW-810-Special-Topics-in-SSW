#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This program defines a Fraction class with basic arithmetic functions.  It also provides a test_suite function
    allowing user's to quickly verify the functions preform correctly
"""
__author__ = "Will DeRoberts"
__date__ = "May 17th, 2020"


class Fraction:
    """ A Fraction consists of a numerator and a denominator.  This class provides functions allowing a user to
    perform basic arithmetic using fractions """

    def __init__(self, num: int, denom: int) -> None:
        try:
            self.numerator: int = int(num)
        except ValueError:
            raise ValueError(f"'{num}' must be a number")

        try:
            self.denominator: int = int(denom)
        except ValueError:
            raise ValueError(f"'{denom}' must be a number")

        if self.denominator == 0:
            raise ValueError("denominator cannot be 0")

    def set_common_denominator(self, other: "Fraction") -> ("Fraction", "Fraction"):
        """
            returns a pair of new Fractions with a common denominator (this may not be the Least Common Denominator).
            This is computed by:
            -multiplying the numerator/denominator of self by the denominator of other
            -multiplying the numerator/denominator of other by the denominator of self
        """
        if self.denominator != other.denominator:  # multiply each fraction by the other's denominator
            fraction1: Fraction = Fraction(self.numerator * other.denominator, self.denominator * other.denominator)
            fraction2: Fraction = Fraction(other.numerator * self.denominator, other.denominator * self.denominator)
            return fraction1, fraction2
        else:  # already have a common denominator
            return self, other

    def plus(self, other: "Fraction") -> "Fraction":
        """ returns a new instance of class Fraction with the sum of self and other where other is another Fraction """
        fraction1, fraction2 = self.set_common_denominator(other)
        return Fraction(fraction1.numerator + fraction2.numerator, fraction1.denominator)

    def minus(self, other: "Fraction") -> "Fraction":
        """ return a new instance of class Fraction with the difference of self and other where other is another
        Fraction """
        fraction1, fraction2 = self.set_common_denominator(other)
        return Fraction(fraction1.numerator - fraction2.numerator, fraction1.denominator)

    def times(self, other: "Fraction") -> "Fraction":
        """ return a new instance of class Fraction with the product of self and other where other is another
        Fraction """
        new_numerator: int = self.numerator * other.numerator
        new_denominator: int = self.denominator * other.denominator

        return Fraction(new_numerator, new_denominator)

    def divide(self, other: "Fraction") -> "Fraction":
        """ return a new instance of class Fraction with the quotient of self and other where other is another
        Fraction """
        new_numerator: int = self.numerator * other.denominator
        new_denominator: int = self.denominator * other.numerator

        if new_denominator == 0:
            raise ZeroDivisionError("cannot divide by 0")

        return Fraction(new_numerator, new_denominator)

    def equal(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are equal """
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"


def test_suite() -> None:
    """ runs a suite of unit tests verifying that Fraction initialization works properly as well as the functions:
    plus, minus, times, divide, and equal """

    try:
        f10: Fraction = Fraction(1, 0)
    except ValueError as e:
        if e.__str__() == "denominator cannot be 0":
            print("The exception for initializing an instance with denominator 0 is successful")

    f12: Fraction = Fraction(1, 2)
    f34: Fraction = Fraction(3, 4)
    fm68: Fraction = Fraction(-6, 8)
    f01: Fraction = Fraction(0, 1)
    f44: Fraction = Fraction(4, 4)
    f128: Fraction = Fraction(12, 8)
    f32: Fraction = Fraction(3, 2)
    f912: Fraction = Fraction(9, 12)

    # Test plus function
    print(f"{f12} + {f34} = {f12.plus(f34)} [10/8]")
    print(f"{f12} + {fm68} = {f12.plus(fm68)} [-4/16]")
    print(f"{f12} + {f01} = {f12.plus(f01)} [1/2]")
    print(f"{f12} + {f34} + {f44} = {f12.plus(f34).plus(f44)} [72/32]")

    # Test minus function
    print(f"{f34} - {f44} = {f34.minus(f44)} [-1/4]")
    print(f"{f32} - {f128} = {f32.minus(f128)} [0/16]")
    print(f"{f912} - {f12} = {f912.minus(f12)} [6/24]")
    print(f"{f32} - {fm68} - {f44} = {f32.minus(fm68).minus(f44)} [80/64]")

    # Test times function
    print(f"{f12} * {f34} = {f12.times(f34)} [3/8]")
    print(f"{f12} * {fm68} = {f12.times(fm68)} [-6/16]")
    print(f"{f12} * {f01} = {f12.times(f01)} [0/2]")
    print(f"{f12} * {f34} * {f44} = {f12.times(f34).times(f44)} [12/32]")

    # Test divide function
    print(f"{f12} / {f34} = {f12.divide(f34)} [4/6]")
    print(f"{f12} / {fm68} = {f12.divide(fm68)} [8/-12]")
    try:
        print(f"{f12} / {f01} = {f12.divide(f01)} [0/2]")
    except ZeroDivisionError:
        print("The exception for dividing a fraction by 0 is successful")
    print(f"{f12} / {f34} / {f44} = {f12.divide(f34).divide(f44)} [16/24]")

    # Test the equal function
    print(f"{f12} == {f12} is {f12.equal(f12)}[True]")
    print(f"{f34} == {f912} is {f34.equal(f912)}[True]")
    print(f"{f12} == {f34} is {f12.equal(f34)}[False]")


def get_number(prompt: str) -> int:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return int(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")


def get_operator(prompt: str) -> str:
    """ read and return an operator from the user.
            Loop until the user provides a valid operator.
    """
    while True:
        inp: str = input(prompt)
        if inp in ['+', '-', '*', '/', '==']:
            return inp
        else:
            print(f"Error: '{inp}' is not a valid operator. Please try again...")


def compute(f1: Fraction, operator: str, f2: Fraction) -> "Fraction":
    """ computes a new Fraction by applying the operator to the passed Fractions.  Supported operators are: +, -, *,
    /, and == """

    if operator == '+':
        return f1.plus(f2)
    if operator == '-':
        return f1.minus(f2)
    if operator == '*':
        return f1.times(f2)
    if operator == '/':
        try:
            return f1.divide(f2)
        except ZeroDivisionError:
            raise ZeroDivisionError

    if operator == '==':
        return f1.equal(f2)

    raise ValueError("ERROR: unrecognized operator type")


def main() -> None:
    """ asks the user for the first numerator and denominator, the operator, and the second numerator and
    denominator, then prints the result of applying the operator to the two fractions. """

    print("Welcome to the fraction calculator!")
    while True:
        try:
            f1: Fraction = Fraction(get_number("Fraction 1 numerator: "), get_number("Fraction 1 denominator: "))
            break
        except ValueError as e:
            print(f"{e}, please try again")

    operator: str = get_operator("Operation (+, -, *, /, ==): ")

    while True:
        try:
            f2: Fraction = Fraction(get_number("Fraction 2 numerator: "), get_number("Fraction 2 denominator: "))
            break
        except ValueError as e:
            print(f"{e}, please try again")

    try:
        print(f"{f1} {operator} {f2} = {compute(f1, operator, f2)}")
    except ZeroDivisionError:
        print("Undefined - cannot divide by 0")


if __name__ == '__main__':
    # test_suite()
    main()
