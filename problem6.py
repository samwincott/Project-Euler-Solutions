def sum_of_squares(n):

	total = 0
	for i in range(1, n+1):
		total += i * i

	return total

def square_of_sum(n):

	total = sum(range(1,n+1)) ** 2

	return total

n = 10
squares_summed = sum_of_squares(n)
sum_squared = square_of_sum(n)
difference = sum_squared - squares_summed

print("The sum of the squares of the first %i natural numbers is %i\n"
	"The square of the sum of the first %i natural numbers is %i\n"
	"The sum of the squares of the first %i natural numbers is %i"
	% (n, squares_summed, n, sum_squared, n, difference))