def generate_prime_numbers(val):
	if type(val) is not type(0):
		raise TypeError('Value is not an integer')
	elif val < 0:
		raise ValueError('Value given is out of range')
	else:
		primes = []
		for x in range(1, val+1):
			err = 0
			for y in range(1, x):
				if x%y == 0:
					err = err + 1
					if err > 1 :
						break
			if err is 1:
				primes.append(x)
		return primes
