def isPalindrome(inputString):

	inputString = str(inputString)
	
	if inputString == inputString[ : : -1]:
		return True
	else:
		return False

palindromeList = []

for x in range(100, 1000):
	for y in range(100, 1000):
		product = x * y
		if isPalindrome(product):
			palindromeList.append(product)

print(max(palindromeList))

