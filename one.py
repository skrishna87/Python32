print('hello')

def func():
	print('func() in one.py')

print('top level in one.py')

if __name__ == '__main__':
	print('one.py is being run ditectly')

else:
	print('one.py has imported!')
