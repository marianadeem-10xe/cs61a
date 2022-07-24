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
def yiip(signal, bookbook):
    if signal < 0:
        return bookbook(3,signal)
    elif signal == 0:
        return float("inf")
    return signal * -98

def yip(mup, pet):
    if mup<0:       # other options are true as well
        mup += 1
    if mup==pet:
        return lambda al: lambda fal: mup**al+pet**fal  
                        
    return lambda al: lambda fal: al - fal

yuiop = yiip(-2, yip)(3)(5)

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
    def count_digit(target, n):
        """counts the number of times TARGET integer appears in N"""
        count=0
        while n:
            if target==n%10:
                count+=1
            n = n//10
        return count
    # base case:
    if n==0:
        return 0
    else:
        if str(10-n%10) in str(n//10):
            return count_digit(10-n%10, n//10) + ten_pairs(n//10)
        return ten_pairs(n//10)          

#Q10. Num-Split
def num_splits(s, d):
    """Return the number of ways in which s can be partitioned into two
    sublists that have sums within d of each other.

    >>> num_splits([1, 5, 4], 0)  # splits to [1, 4] and [5]
    1
    >>> num_splits([6, 1, 3], 1)  # no split possible
    0
    >>> num_splits([-2, 1, 3], 2) # [-2, 3], [1] and [-2, 1, 3], []
    2
    >>> num_splits([1, 4, 6, 8, 2, 9, 5], 3)
    12
    """
    "*** YOUR CODE HERE ***"
    def subsets(lst):
        subset = [[]]
        for i in range(len(lst)-1, -1, -1):
            subset+= [[lst[i]]+sublst for sublst in subset]
        return subset    
    
    count= 0
    s_copy = s[:]
    for sub1 in subsets(s):
        [s_copy.remove(e) for e in sub1]
        sub2 = s_copy 
        if abs(sum(sub1)-sum(sub2))<=d:
            count+=1
        s_copy= s[:]
    return count//2

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
    if is_leaf(t):
        return None if label(t) in vals else t
    else:
        bs = []
        for b in branches(t):
            if prune_leaves(b, vals):
                bs.append(prune_leaves(b, vals))
        return tree(label(t), bs)

# Q12. Hailstone Tree
def hailstone_tree(n, h):
    """Generates a tree of hailstone numbers that will reach N, with height H.
    >>> print_tree(hailstone_tree(1, 0))
    1
    >>> print_tree(hailstone_tree(1, 4))
    1
        2
            4
                8
                    16
    >>> print_tree(hailstone_tree(8, 3))
    8
        16
            32
                64
            5
                10
    """
    
    if ((n-1)%3!=0 or n in [4,2,1]) and h!=0:
        return tree(n, [hailstone_tree(n*2, h-1)]) 
    branches = []
    if h!=0 and (n-1)%3==0 and n%2==0:
        branches += [hailstone_tree(n*2, h-1), hailstone_tree((n-1)//3, h-1)]
    return tree(n, branches)


def print_tree(t):
        def helper(i, t):
            print("    " * i + str(label(t)))
            for b in branches(t):
                helper(i + 1, b)
        helper(0, t)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])    