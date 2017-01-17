import unittest;

from prime import generate_prime_numbers

class GeneratePrimeTest(unittest.TestCase):
	def test_input_is_integer(self):
		with self.assertRaises(TypeError):
			generate_prime_numbers("5")

	def test_output_is_list(self):
		self.assertEquals(type([]), type(generate_prime_numbers(20)), msg="Does not produce list")

	def test_output_has_integers(self):
		self.assertEquals(type(0), type(generate_prime_numbers(15)[2]), msg="Output list does not have non integers")

	def test_output_has_only_positive_integers(self):
		with self.assertRaises(ValueError):
			generate_prime_numbers(50).index(-1)

	def test_output_does_not_contain_number_one(self):
		with self.assertRaises(ValueError):
			generate_prime_numbers(50).index(1)
