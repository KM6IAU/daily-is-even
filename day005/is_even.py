def is_even(val:int):
	for char in str(val):
		digit_is_even = True if char in ['0','2','4','6','8'] else False
	return digit_is_even
