from unittest import TestCase
import generate_prime_numbers


class TestPrimeGenerator(TestCase):
    def setUp(self):
        self.prime_gen = generate_prime_numbers(1)

    def test_is_integer(self):
        self.assertIsInstance(self.prime_gen.n, int, msg="Value not an integer")

    def test_not_negative(self):
        self.assertGreater(self.prime_gen.n, 0, msg="Value not positive integer")

    def test_is_greater_than_or_equal_to_two(self):
        self.assertGreater(self.prime_gen.n, 2, msg="Value not in the prime number scope")

    def test_is_output_a_list_of_integers(self):
        self.assertTrue(any(isinstance(x, int) for x in self.prime_gen.generate_prime_numbers()), msg="Output is not a list of integers")

    def test_is_output_a_list(self):
        self.assertTrue(isinstance(self.prime_gen.generate_prime_numbers(), list), msg="Output is not a list")