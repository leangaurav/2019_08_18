class Contact:
	def __init__(self, name, phone, email = ''):
		self.name = name
		self.phone = phone
		self.email = email

	def __str__(self):
		return "Name:{} Phone:{} Email:{}".format(self.name, self.phone, self.email)
		
	def __repr__(self):
		return str(self)

	def match_name(self, pattern):
		return pattern.lower() in self.name.lower()
		
if __name__ == "__main__":
	c1 = Contact('abc','11111111')
	c2 = Contact('pqr','22222222222222', "ab@cd.com")
	
	print(c1, c2)
	print(c1.match_name('ABC'))
	print(c1.match_name('BC'))
	print(c1.match_name('DBC'))
	print(c2.match_name('pqr'))
