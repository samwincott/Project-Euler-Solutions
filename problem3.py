def primeFactors(n):

	factorList = []
	factorTest = 2

	while n >= (factorTest / 2):
		if n % factorTest == 0:
			factorList.append(factorTest)
			n /= factorTest
		else:
			factorTest += 1
	return factorList

largeNumber = 600851475143
primeFactorsList = primeFactors(largeNumber)

print("The highest prime factor of %i is %i" % (largeNumber, primeFactorsList[-1]))

