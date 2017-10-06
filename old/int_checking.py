__author__ = 'Bryce Ogden'


def consecutive_ints(aString):
	""" 
	Takes a string and parses for integers, 
	returning True or False if two numbers are next to each other 
	e.g. "CAT1 DOG2" is False / "COW123" is True
	"""
	counter = 0
	indexes = []
	# iterate through 'aString' to see if integers exist
	for i in range( len(aString) ):
		if is_int( aString[i] ):
			counter += 1
			indexes.append(i)

	# iterate through int indexes of 'aString'
	trueFlag = 0
	if len(indexes) > 0:
		prev = None
		for i in range( len(indexes) ):
			try:
				prev = indexes[i-1]
				if indexes[i] - prev == 1:
					trueFlag = 1
					break
			except IndexError as e:
				pass

	return True if trueFlag == 1 else False
 




def is_int(letter):
	""" 
	Takes a string argument that returns true if 
	a valid integer or false if not 
	e.g. "7" is True / "a" is False / "1.0" is False
	"""
	works = False
	try:
		int(letter)
		works = True
	except ValueError as e:
		pass
	finally:
		return works
