def fibonacci(n) :

	a = 1
	b = 1

	if n < 0 :
		print("Incorrect input")
	elif n == 0 :
		return a
	elif n == 1 :
		return b
	else : 
		for i in range(2, n+1):
			c = a + b
			a = b
			b = c
		return b

tempAnswer = 0
counter = 1
total = 0
while tempAnswer <= 4000000 :
	tempAnswer = fibonacci(counter)
	if tempAnswer % 2 == 0 :
		total += tempAnswer
	counter += 1

print(total)