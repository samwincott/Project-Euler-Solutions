def is_prime(n):

	for divisor in range(2, n):
		if n % divisor == 0:
			return False

	return True

def first_n_primes(n):

	primes_list = []
	counter = 2
	while len(primes_list) < n:
		if is_prime(counter):
			primes_list.append(counter)
		counter += 1

	return primes_list

n = 10001
first_n_primes_list = first_n_primes(n)

print("The number %ist prime number is %i" % (n, first_n_primes_list[-1]))
