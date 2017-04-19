from unittest import TestCase
from generate_prime_numbers import generateprimenumbers

class TestPrimeGenerator(TestCase):
    def test_correct_output(self):
        self.assertListEqual([2, 3, 5, 7], generateprimenumbers(10))

    def test_one_in_result(self):
        self.assertFalse(1 in generateprimenumbers(10), msg='1 is not a prime number')

    def test_zero_in_result(self):
        self.assertFalse(0 in generateprimenumbers(10), msg='0 is not a prime number')

    def test_two_in_result(self):
        self.assertTrue(2 in generateprimenumbers(10), msg='2 is a prime number')

    def test_non_prime_number_divisible_by_3(self):
        self.assertFalse(9 in generateprimenumbers(10), msg='9 is divisible by 3')