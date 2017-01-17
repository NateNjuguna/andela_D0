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
			
	def test_generate_prime_test_works(self):
		self.assertEquals([2, 3, 5, 7], generate_prime_numbers(10), msg="generate prime test doesn't work as expected")
		
	def test_input_is_not_less_than_0(self):
		with self.assertRaises(ValueError):
			generate_prime_numbers(-1)
		
	def test_input_is_not_0(self):
		with self.assertRaises(ValueError):
			generate_prime_numbers(0)
	
	def test_output_is_string_for_no_primes(self):
		self.assertEquals(type(generate_prime_numbers(1)), type(''), msg="Expected string for no primes")
	
	def test_output_is_string_no_primes_for_no_primes(self):
		self.assertEquals(generate_prime_numbers(1), 'no primes', msg="Expected string 'no primes' for no primes")
		
	
