class A:
    def funct1(self):
        print("A:funct1")
    def funct2(self):
        print("A:funct2")
        
        
class B(A):
    def funct3(self):
        print("B:funct3")
    
ob1 = B()
ob1.funct1()
ob1.funct2()

ob1.funct3()

ob2 = A()
ob2.funct1()
#ob2.funct3()