from point import Point
from shape import Shape

class Rectangle(Shape):
    def __init__(self, points):
        super().__init__(4, points)
        
if __name__ == '__main__':
    p = [Point(10,10),
     Point(10,15),
     Point(15,10),
     Point(10,20)]
     
    r1 = Rectangle(p)
    print(r1)
    
    p.pop()
    r2 = Rectangle(p)
    print(r2)