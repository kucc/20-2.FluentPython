import math

class Point:

    def __init__(self, x=0, y=0):   # for `Point(1, 2)`
        """the constructor"""
        self.x = x
        self.y = y


    # two methods related to string
    def __repr__(self):
        """the string representation of the object
        It will be shown useful in interactive mode

        invariant: eval(repr(obj)) == obj
        """
        return 'Point(%r, %r)' % (self.x, self.y)

    def __str__(self):
        """If not defined, str() will call __repr__
        This is for end user, such as pretty-printing functionality
        """
        return '(%s, %s)' % (str(self.x), str(self.y))
    

    # binary operator must not change the input
    def __add__(self, other):    # for `Point(1, 2) + Point(3, 4)`
        """for `obj1 + obj2`"""
        x = self.x + other.x
        y = self.y + other.y


        return Point(x, y)

    def __mul__(self, scalar):   # for `Point(1, 2) * 3`
        """for scalar multiplication
        This does not support commutative property
        """
        return Point(scalar * self.x, scalar * self.y)

    def __eq__(self, other):    # for `Point(1, 2) == Point(1, 2)`
        """compare if two are equal"""
        return (self.x == other.x) and (self.y == other.y)

    def __abs__(self): 
        return math.sqrt(self.x * self.x + self.y * self.y)










if __name__ == "__main__":
    p1 = Point(3, 4)
    p2 = Point(2, 4)
    p3 = p1 + p2
    p4 = p1 * 2
    # p5 = 2 * p1  # Error

    # This will call `p1.__str__`
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print('')

    # difference between `__repr__` and `__str__`
    p1_repr = repr(p1)
    p1_str = str(p1)

    print('p1_repr: %s' % format(p1_repr))
    print('p1_str: %s' % format(p1_str))
    print('eval(repr(p1)) == p1: %r' % format(eval(repr(p1)) == p1))
    print('eval(repr(p1)) == p1: %s' % format(eval(repr(p1)) == p1))
    # print('eval(str(p1)) == p1: %r' % format(eval(str(p1)) == p1))

    print('abs(%r): %r' % (p1, abs(p1)))

