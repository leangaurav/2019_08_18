from point import Point
from shape import Shape

class Triangle(Shape):
    def __init__(self, points):
        super().__init__(3, points)
        
    def __str__(self):
        return "Triangle\n" + super().__str__()
        
if __name__ == '__main__':
    p = [Point(10,10),
     Point(10,15),
     Point(15,10)]
     
    r1 = Triangle(p)
    print(r1)
    
    p.pop()
    r2 = Triangle(p)
    print(r2)