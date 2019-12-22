class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "x:{} y:{}".format(self.x, self.y)
        
if __name__ == '__main__':
    p1 = Point(10,20)
    print(p1)