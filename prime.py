def generate_prime_numbers(val):
	if type(val) is not type(0):
		raise TypeError('Value is not an integer');
	else:
		primes = []
		for x in range(0, val+1):
			for y in range(1, val):
				if x%y is 0:
					break
			primes.append(x)
		return primes
