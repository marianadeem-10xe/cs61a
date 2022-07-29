class Bear(object):
    """ A Bear. """

    def __init__(self):
        self.__repr__ = lambda: "oski"
        self.__str__  = lambda: "this very bear"

    def __repr__(self):
        return "Bear()"

    def __str__(self):
        return "a bear"

oski = Bear()
print(oski)
print(str(oski))
print(repr(oski))
print(oski.__str__())
print(oski.__repr__())
print()

def our_repr(x):
    return type(x).__repr__(x)

def our_str(x):
    t = type(x) # class of x
    if hasattr(t, "__str__"):
        return t.__str__(x)
    else:
        return our_repr(x)

print(oski)
print(our_str(oski))
print(our_repr(oski))
print(oski.__str__())
print(oski.__repr__())
print()

from math import gcd
class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        """
        >>> repr(Ratio(1, 2))
        'Ratio(1, 2)'
        """
        #return "Ratio("+str(self.numer)+", " + str(self.denom) + ")"
        return f"Ratio({self.numer}, {self.denom})"

    def __str__(self):
        """
        >>> str(Ratio(1, 2))
        '1/2'
        """
        return f"{self.numer}/{self.denom}"

    def __add__(self, other):
        """
        >>> Ratio(1, 2) + Ratio(1, 2)
        Ratio(1, 1)
        >>> 1 + Ratio(1, 2)
        Ratio(3, 2)
        >>> Ratio(1, 2) + 10
        Ratio(21, 2)
        >>> 1 + Ratio(1, 2)
        Ratio(3, 2)
        >>> 0.5 + Ratio(1, 2)
        1.0
        """
        if isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, float):
            return float(self) + other
        else:
            raise TypeError(f"bad operand type for +: {type(other)}")
        g = gcd(n, d)
        return Ratio(n // g, d // g)

    __radd__ = __add__

    def __float__(self):
        return self.numer/self.denom
def invert(x):
    y = 1/x
    print("Never print if x is 0")
    return y

def invert2(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print('handled', e)
        return 0
    except TypeError as e:
        print("Pass in the correct type please!, we only accept numbers")
    except NameError as e:
        print("Make sure you called invert! Check your code Alex")
""" DO NOT DO THIS """
def invert3(x):
    try:
        return invert(x)
    except BaseException as e: # Always use the most specific type of exception
        print(e), print(type(e)), print(str(e)), print(repr(e))
        print('handled', e)
        return 0

for i in range(5):
    print(i)

my_it = iter(range(5))
try:
    while True:
        i = next(my_it)
        print(i)
except StopIteration as e:
    pass

from operator import mul
def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).

    >>> reduce(mul, [2, 4, 8], 1)
    64
    """
    if len(s) == 0:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce(f, rest, f(initial, first))

def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8).

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [1, 2, 3, 4], 2)
    16777216
    """
    for x in s:
        initial = f(initial, x)
    return initial

from operator import truediv
def divide_all(n, ds):
    """ Divide n by every number in ds

    >>> divide_all(1024, [2, 4, 8])
    16.0
    """
    try:
        return reduce(truediv ,ds, n)
    except ZeroDivisionError:
        return float('inf') * n/abs(n)
