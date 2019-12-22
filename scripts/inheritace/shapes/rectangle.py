from point import Point

class Rectangle:
    def __init__(self, points):
        if len(points) != 4:
            raise ValueError("Need 4 points")
        self.points = points
        
    def __str__(self):
        return ("Point:{} "*4).format(*self.points)
        
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