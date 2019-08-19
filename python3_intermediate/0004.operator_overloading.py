class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    #

    def __str__(self):
        return 'Point({0},{1})'.format(self.x, self.y)
    #

    def magnitude(self):
        return self.x ** 2 + self.y ** 2
    #

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()
    #

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    #

    def __iadd__(self, other):
        x = self.x + other[0]
        y = self.y + other[1]
        return Point(x, y)
    #

    def __isub__(self, other):
        x = self.x - other[0]
        y = self.y - other[1]
        return Point(x, y)
    #
#


if __name__ == '__main__':
    p1 = Point(2, 3)
    p2 = Point(-1, 2)
    print(p1 + p2)
    print(p1 < p2)

    p1 += (4, 2)
    print(p1)
    p2 -= (-5, -3)
    print(p2)
#