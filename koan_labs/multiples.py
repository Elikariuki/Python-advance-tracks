def multiple_sum():
	#TODO: Your code goes 
	numbers = []
	for i in range(1, 1000):
		if i % 3 == 0 or i % 5 == 0:
			numbers.append(i)
	return sum(numbers)
	