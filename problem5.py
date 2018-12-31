def greatestCommonDenominator(a, b):

	while(b): 
		a, b = b, a % b 

	return a

def lowestCommonMultiple(a, b):

	gcd = greatestCommonDenominator(a, b)
	lcm = (a * b) / gcd
	
	return lcm

answer = 1
for i in range(1, 21):
	answer = lowestCommonMultiple(answer, i)

print("The answer is %i" % (answer))