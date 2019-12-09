class Test:
	def __init__(self, val):
		self.val = val
		print("init called", self.val)
		
	def __del__(self):
		print("Del called", self.val)

print("Creating t1")
t1 = Test(1)
# reference count
print("Copying t1")
t2 = t1
print("Creating t3")
t3 = Test(3)

print("Deleting t3")
del t3
print("Deleting t1")
del t1
del t2
print("End")



