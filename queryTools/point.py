class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

if __name__ == '__main__':
    a = Point(3,4)
    b = Point(1,1)

    print(a-b)
    print(b * 3)
