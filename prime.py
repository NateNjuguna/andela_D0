import big_o

def generate_prime_numbers(val):
	if type(val) is not type(0):
		raise TypeError('Value is not an integer')
	elif val < 1:
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
		return primes if len(primes) > 0 else 'no primes'

generator = lambda n: big_o.datagen.n_(1000)
best_case, other_cases = big_o.big_o(generate_prime_numbers, generator, n_repeats=100)

for class_, residuals in other_cases.items():
	print class_, '   (res: %.2G)' % residuals
	
print best_case
