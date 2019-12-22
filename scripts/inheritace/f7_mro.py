class A:
    def funct1(self):
        print("A:funct1")
        
class B(A):
    def funct1(self):
        print("B:funct1")
        super().funct1()
        
class C(A):
    def funct1(self):
        print("C:funct1")
        super().funct1()

class D(A):
    def funct1(self):
        print("D:funct1")
    
class E(B,C):
    def funct1(self):
        print("E:funct1")
        super().funct1()
        
class F(C,D):
    def funct1(self):
        print("F:funct1")
        super().funct1()
        
class G(A,E):
    pass

"""
                A
            /   |   \
           /    |    \
       B(s)    C(s)     D
           \  /    \   /
            E        F
"""
e1 = E()
e1.funct1()

print()
f1 = F()
f1.funct1()

print(E.mro())
