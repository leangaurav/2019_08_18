class A:
    def __init__(self,x):
        self.a = x

class B(A):
    def __init__(self):
        super().__init__(10) # need to call parent __init__ explicitly
        self.b = 100000
    

#ob1 = B(10)
ob1 = B()
print(ob1.a)
print(ob1.b)