def sumOfMultiples(multiplesOf, target):
	total = 0
	for counter in range(target):
		for multiple in multiplesOf:
			if counter % multiple == 0:
				total += counter
				break
	return total

print(sumOfMultiples([3,5], 1000))
