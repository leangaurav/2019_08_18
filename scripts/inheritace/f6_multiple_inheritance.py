class A:
    def funct1(self):
        print("A:funct1")
        
class B:
    def funct1(self):
        print("B:funct1")
        
class C(B,A):
    pass
class D(A,B):
    pass
    
class E(A,B):
    def funct1(self):
        super().funct1()
        print("E:funct1")

print(C.__bases__)    
c1 = C()
c1.funct1()

print()
d1 = D()
d1.funct1()

print()
e1 = E()
e1.funct1()
