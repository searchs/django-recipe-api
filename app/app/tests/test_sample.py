from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_add_neg_numbers(self):
        """Test adding negative numbers together"""
        res = calc.add(-5, -2)
        self.assertEqual(res, -7)

    def test_subtract_numbers(self):

        res = calc.subtract(10, 16)
        self.assertEqual(res, 6)
