from point import Point

class Triangle:
    def __init__(self, points):
        if len(points) != 3:
            raise ValueError("Need 3 points")
        self.points = points
        
    def __str__(self):
        return ("Point:{} "*3).format(*self.points)
        
if __name__ == '__main__':
    p = [Point(10,10),
     Point(10,15),
     Point(15,10)]
     
    r1 = Triangle(p)
    print(r1)
    
    p.pop()
    r2 = Triangle(p)
    print(r2)