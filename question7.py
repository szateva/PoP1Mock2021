# 13021326

class My_integer:
    def __init__(self, x):
    #method creates My_integer object that represents
    #a usual Python integer x
        self.x = x

    def increase(self, o):
    #method increases the value of this object by the
    #value represented by another My_integer object o;
    #method returns nothing
        self.x += o.x

    def plus(self, o):
        sum = My_integer(self.x + o.x)
        return sum
    #method returns the My_integer object representing
    #the sum of the value represented by this object and
    #the value represented by My_integer object o
    def __eq__(self, other):
        if self.x == other.x:
            return True
        else:
            return False

a = My_integer(20)
b = My_integer(364)
c = a.plus(b)
d = My_integer(182)
a.increase(d)
assert not a == c  # must be True
a.increase(d)
assert a == c  # must be True
