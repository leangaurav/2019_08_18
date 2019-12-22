class A:
    def __init__(self,x):
        self.a = x

class B(A):
    pass
    

ob1 = B(10)
print(ob1.a)