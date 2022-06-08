#!/usr/bin/env python3
# unit test for a given daily is_even()



from day005.is_even import is_even



def test():
	result = False
	try:
		assert(  is_even(          -2 ) == True   )
		assert(  is_even(          -1 ) == False  )
		assert(  is_even(           0 ) == True   )
		assert(  is_even(           1 ) == False  )
		assert(  is_even(           2 ) == True   )
		assert(  is_even(      0x1000 ) == True   )
		assert(  is_even(      0x1001 ) == False  )
		assert(  is_even(  0x0FFFFFFF ) == False  )
		assert(  is_even(  0x10000000 ) == True   )
		assert(  is_even(  0x10000001 ) == False  )
		result = True
	except AssertionError: print ("Assertion error.")
	except Exception as e: print ("Unexpected error: \"" + str(e) + "\"")
	return result



print (   "success = " + str(  test()  )   )
