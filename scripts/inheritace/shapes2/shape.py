from point import Point

class Shape:
    def __init__(self, no_of_points, points):
        if (no_of_points != len(points)):
            raise ValueError("Points len should be %d" % (no_of_points))
        self.no_of_points = no_of_points
        self.points = points
        
    def __str__(self):
        return ("{}\n"+"Point:{} " * self.no_of_points ).format(self.__class__.__name__, *self.points)
        
if __name__ == '__main__':
    s1 = Shape(2, [Point(1,2), Point(2,3)])
    print(s1)
    s2 = Shape(2, [Point(1,2)])
    print(s2)