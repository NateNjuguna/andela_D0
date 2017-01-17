import unittest;

from prime import generate_prime_numbers

class TestGeneratePrime(unittest.TestCase):
  def test_input_is_integer(self):
    with self.assertRaise(TypeError):
      generate_prime_numbers("5")
