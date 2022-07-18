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
        val = start
        for e in s:
            val = f(val, e)
        return val

# Q7. Announce losses: see hog.py
# Q8. Pig Latin
def pig_latin_original(w):
    """Return the Pig Latin equivalent of a lowercase English word w."""
    if starts_with_a_vowel(w):
        return w + 'ay'
    else:
        vowels_found = any([starts_with_a_vowel(l) for l in w])
        if not vowels_found:
            return w + "ay" 
    return pig_latin_original(rest(w) + first(w))

def first(s):
    """Returns the first character of a string."""
    return s[0]

def rest(s):
    """Returns all but the first character of a string."""
    return s[1:]

def starts_with_a_vowel(w):
    """Return whether w begins with a vowel."""
    c = first(w)
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'

# Q9: Ten-pairs
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"

# Q11: Pruning Leaves
def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label
    that appears in vals removed.  Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    "*** YOUR CODE HERE ***"
    if 
     