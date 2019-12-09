class Singleton2:
	__dict = {}
	def __new__(cls,*args, **kwargs):
		obj = super().__new__(cls,*args, **kwargs)
		obj.__dict__ = Singleton2.__dict
		return obj

s1 = Singleton2()
s2 = Singleton2()

print(s1, s2)
s1.x = 10000
print(s2.x)
