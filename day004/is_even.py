def is_even(val:int):
	return True if abs(val) in range(0, abs(val)+1, 2) else False
