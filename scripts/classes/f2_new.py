class Test:

	def __new__(cls, *args, **kwargs):
		obj = super().__new__(cls,*args, **kwargs)
		print("New ", obj)
		return obj
	
	def __init__(self):
		print("init called")

t1 = Test()
t2 = Test()