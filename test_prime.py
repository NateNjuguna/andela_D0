import unittest;

from prime import generate_prime_numbers

class GeneratePrimeTest(unittest.TestCase):
	def test_input_is_integer(self):
		with self.assertRaises(TypeError):
			generate_prime_numbers("5")
