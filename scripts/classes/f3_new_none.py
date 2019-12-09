class Test:

	def __new__(cls, *args, **kwargs):
		print("New ")
		return None
	
	def __init__(self):
		print("init called")

class Test1:

	def __new__(cls, *args, **kwargs):
		print("New ")
		return 1
	
	def __init__(self):
		print("init called")

		
if __name__ == '__main__':
	t1 = Test()
	print("main", t1)
	t2 = Test()
	print("main", t1)


	t1 = Test1()
	print("main", t1)
	t2 = Test1()
	print("main", t1)