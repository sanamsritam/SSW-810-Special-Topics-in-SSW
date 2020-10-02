"""
Author: Sanam Jena
CWID:10454295
Date: 25 Sept 2020
Objective: To write test class for HW2
"""

import unittest
from HW03_Sanam_Jena import Fraction


class TestFraction(unittest.TestCase):
    """[This is the test class inside which we have all the various tests written.]

    Args:
        unittest ([type])
    """

    def test1_init(self) -> None:
        """[In this function we are checking if the fraction is getting initialized properly or not.]
        """
        f: "Fraction" = Fraction(1, 4)
        self.assertEqual(f.numerator, 1)
        self.assertEqual(f.denominator, 4)

    def test2_init_exception(self) -> None:
        """[In this function we are testing if a ValueError is raised or not when we try to set the denominator the fraction as 0(Zero).]
        """
        with self.assertRaises(ValueError, msg="The denominator of a fraction cannot be ZERO, Try Again!"):

            f10: "Fraction" = Fraction(1, 0)

    def test3_add(self) -> None:
        """[In this function we are testing the magic function __add__ where in perform the operation of addition]
        """
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        self.assertEqual(f12 + f13, Fraction(5, 6))
        self.assertNotEqual(f12 + f13, Fraction(12, 89))

    def test4_multiple_operands(self) -> None:
        """ This Function verifies Fraction addition with more than two operands"""
        f12: "Fraction" = Fraction(1, 2)
        f32: "Fraction" = Fraction(3, 2)
        f68: "Fraction" = Fraction(6, 8)
        f13: "Fraction" = Fraction(1, 3)
        self.assertEqual(f12 + f12 + f12, Fraction(12, 8))
        self.assertEqual(f13 + f13 + f13, Fraction(3, 3))
        self.assertEqual(f12 + f32 * f68, Fraction(52, 32))

    def test5_sub(self) -> None:
        """[In this function we are testing the magic function __sub__ where in perform the operation of subtraction ]
        """
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        f13: "Fraction" = Fraction(1, 3)
        self.assertEqual(f12 - f13, Fraction(1, 6))
        self.assertNotEqual(f12 - f34 - f13, Fraction(-15, 24))

    def test6_mul(self) -> None:
        """[In this function we are testing the magic function __mul__ where in perform the operation of multiplication]
        """
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        f34: "Fraction" = Fraction(3, 4)
        self.assertEqual(f12 * f34, Fraction(3, 8))
        self.assertEqual(f12 * f13, Fraction(1, 6))
        self.assertEqual(f12 * f34 * f13, Fraction(3, 24))

    def test7_truediv(self) -> None:
        """[In this function we are testing the magic function __truediv__ where in perform the operation of division]
        """
        f12: "Fraction" = Fraction(1, 2)
        f68: "Fraction" = Fraction(6, 8)
        self.assertEqual(f12 / f68, Fraction(8, 12))
        self.assertNotEqual(f12 / f68, Fraction(9, 12))

    def test8_equal(self) -> None:
        """[In this function we are testing the magic function __eq__ where in we check the equality of the two fractions]
        """
        f12: "Fraction" = Fraction(1, 2)
        f24: "Fraction" = Fraction(2, 4)
        f34: "Fraction" = Fraction(3, 4)
        f68: "Fraction" = Fraction(6, 8)
        self.assertTrue(f12 == f24)
        self.assertFalse(f12 == f34)
        self.assertFalse(f12 == f68)

    def test9_notequal(self) -> None:
        """[In this function we are testing the magic function __ne__ where in we check the inequality of the two fractions]
        """
        f12: "Fraction" = Fraction(1, 2)
        f24: "Fraction" = Fraction(2, 4)
        f48: "Fraction" = Fraction(4, 8)
        f34: "Fraction" = Fraction(3, 4)
        self.assertFalse(f12 != f24)
        self.assertFalse(f12 != f48)
        self.assertTrue(f12 != f34)

    def test10_lessthan(self) -> None:
        """[In this function we are testing the magic function __lt__ where in we check the if fraction f1 is less than fraction f2]
        """
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        f14: "Fraction" = Fraction(1, 4)
        f34: "Fraction" = Fraction(3, 4)
        self.assertLess(f12, f34)
        self.assertEqual(f12.__lt__(f13), False)
        self.assertEqual(f12.__lt__(f14), False)

    def test11_lessthanequal(self) -> None:
        """[In this function we are testing the magic function __le__ where in we check the if fraction f1 is less than or equalto to fraction f2]
        """
        f12: "Fraction" = Fraction(1, 2)
        f34: "Fraction" = Fraction(3, 4)
        f13: "Fraction" = Fraction(1, 3)
        f14: "Fraction" = Fraction(1, 4)
        self.assertLessEqual(f12, f34)
        self.assertLessEqual(f12, f12)
        self.assertEqual(f34.__le__(f12), False)
        self.assertEqual(f12.__le__(f13), False)
        self.assertEqual(f12.__le__(f14), False)

    def test12_greaterthan(self) -> None:
        """[In this function we are testing the magic function __gt__ where in we check the if fraction f1 is greater than fraction f2]
        """
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        f34: "Fraction" = Fraction(3, 4)
        f24: "Fraction" = Fraction(2, 4)
        self.assertGreater(f12, f13)
        self.assertGreater(f34, f12)
        self.assertEqual(f12.__gt__(f12), False)
        self.assertEqual(f12.__gt__(f24), False)

    def test13_greaterthanequal(self) -> None:
        """[In this function we are testing the magic function __ge__ where in we check the if fraction f1 is greater than or equalto to fraction f2]
        """
        f12: "Fraction" = Fraction(1, 2)
        f13: "Fraction" = Fraction(1, 3)
        f24: "Fraction" = Fraction(2, 4)
        f34: "Fraction" = Fraction(3, 4)
        self.assertGreaterEqual(f12, f24)
        self.assertGreaterEqual(f34, f12)
        self.assertGreaterEqual(f34, f13)
        self.assertEqual(f12.__ge__(f34), False)

    def test14_str(self) -> None:
        """[(In this function, we will be checking if the working of the __str__ function)]
        """
        f13: "Fraction" = Fraction(1, 3)
        self.assertEqual(str(f13), "1/3")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
