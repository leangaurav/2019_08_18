class Singleton1:
	__instance = None
	def __new__(cls,*args, **kwargs):
		if Singleton1.__instance == None:
			Singleton1.__instance = super().__new__(cls,*args, **kwargs)
			
		return Singleton1.__instance

s1 = Singleton1()
s2 = Singleton1()

print(s1, s2)
s1.x = 10000
print(s2.x)