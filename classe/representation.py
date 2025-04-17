class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point<{self.x},{self.y}>"
    
    def __eq__(self, point):
        return self.x == point.x and self.y == point.y
    
point1 = Point(4, 6)
print(point1) #<__main__.Point object at 0x000001D4B121A390>

point2 = Point(-8, 10)
print(point2)

point3 = Point(4, 6)
print(point3 == point1)