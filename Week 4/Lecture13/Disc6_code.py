# Discussion 6

# Reverse env diagrams
# Q2. Who - What - When=
def what(f):
    def when(x):
        return f(x)
    return when
def who(n):
    def where(k):
        return 2 * k + n
    return where
y = 3
what(who(y))(4)

# Q3. Yip Yip book 
"""def yiip(signal, bookbook):
    if signal < 0:
        return bookbook(signal,signal)
    elif signal == 0:
        return float("inf")
    return signal * -98

def yip(mup, pet):
    if mup:==
        
        mup += 1
    if mup==pet:
        return lambda al: lambda fal: -2*al*fal - 10  
                        
    return lambda al: lambda fal: al - fal

yuiop = yiip(-2, yip)(3)(5)"""

# Q4. List Comprehention
f = lambda x: [print(i+1) for i in range(x)]
f(10)
print(f)           

# Q5. Deep map
def deep_map_mut(fn, lst):
    """Deeply maps a function over a Python list, replacing each item
    in the original list object.

    Does NOT create new lists by either using literal notation
    ([1, 2, 3]), +, or slicing.

    Does NOT return the mutated list object.

    >>> l = [1, 2, [3, [4], 5], 6]
    >>> deep_map_mut(lambda x: x * x, l)
    >>> l
    [1, 4, [9, [16], 25], 36]
    """
    "*** YOUR CODE HERE ***"
    for idx in range(len(lst)):
        if type(lst[idx])==list:
            deep_map_mut(fn, lst[idx])
        else:
            lst[idx]=fn(lst[idx])         

# Q6: Foldl 
from operator import add, sub, mul

def foldl(s, f, start):
    """Return the result of applying the function F to the initial value START
    and the first element in S, and repeatedly applying F to this result and
    the next element in S until we reach the end of the list.

    >>> s = [3, 2, 1]
    >>> foldl(s, sub, 0)      # sub(sub(sub(0, 3), 2), 1)
    -6
    >>> foldl(s, add, 0)      # add(add(add(0, 3), 2), 1)
    6
    >>> foldl(s, mul, 1)      # mul(mul(mul(1, 3), 2), 1)
    6

    >>> foldl([], sub, 100)   # return start if s is empty
    100
    """
    "*** YOUR CODE HERE ***"
    if not s:
        return start
    else:    
        for idx in range(len(s)):
            if idx==0:
                s[idx] = f(start, s[idx])

        else:
            foldl()
            

    return           