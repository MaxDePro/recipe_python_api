"""
Simplae testing for calculator
"""

from django.test import SimpleTestCase

from . import calc


class CalcTesting(SimpleTestCase):
    """ Test the calc model """
    def test_calc_sum(self):
        res = calc.sum_num(5, 6)

        self.assertEqual(res, 11)

    def test_calc_substract(self):
        res = calc.substract_nums(10, 15)

        self.assertEqual(res, 5)
