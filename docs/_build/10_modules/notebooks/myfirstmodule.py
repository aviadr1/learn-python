print('this is a module')

__all__ = ['important_function', 'x']

def not_so_important():
	"""
	meh
	no really
	not so important
	
	>>> not_so_important()
	0
	
	"""
	return 0

def important_function():
	"""
	meh
	no really
	not so important
	
	>>> important_function()
	'really'
	"""
	return 'really'
	
def add(x,y):
	"""
	>>> add(10,5)
	15
	>>> add(10, add(5, 5))
	20
	"""
	return x+y

if __name__ == '__main__':	
	import doctest
	doctest.testmod()
else:
	print('ive been imported as', __name__)

