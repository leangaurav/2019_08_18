class A:
    def funct1(self):
        print("A:funct1")
    def funct2(self):
        print("A:funct2")
        
        
class B(A):
    pass
    
ob1 = B()
ob1.funct1()
ob1.funct2()