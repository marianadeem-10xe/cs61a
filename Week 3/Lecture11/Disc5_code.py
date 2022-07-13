# Discussion 5:

# Q3: Add this many: 

from gettext import find


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"
    this_many = s.count(x)
    for i in range(this_many):
        s.append(el)
    return 

# Q4: Insert items:
def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst.

    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    idx = [i for i in range(len(lst)) if lst[i]==entry]
    shift_pos = 0
    for position in idx: 
        lst.insert(position+shift_pos+1, elem)
        shift_pos+=1
    return lst        

# Q5. Height of the tree:
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    "*** YOUR CODE HERE ***"

    return max([height(b)+1 for b in branches(t)]) if branches(t) else 0     

# Q6. Maximum path depth
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    "*** YOUR CODE HERE ***"
    return label(t) if is_leaf(t) else max([label(t)+max_path_sum(b) for b in branches(t)])

# Q7. Find path
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    
    if is_leaf(tree):
        return [label(tree)] if label(tree)==x else None
    for b in branches(tree):
        path = [label(tree)]+ find_path(b, x) if bool(find_path(b,x)) else [label(tree), None]
        if x in path:
            return path

# Q8. Exam prep: Perfectly Balanced and Pruned
def sum_tree(t):
    """
    Add all elements in a tree.

    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    "*** YOUR CODE HERE ***"
    return label(t) + sum([sum_tree(b) for b in branches(t)])

def balanced(t):
    """
    Checks if each branch has same sum of all elements,
    and each branch is balanced.

    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(t, [t, tree(1)])
    >>> balanced(t)
    False
    """
    "*** YOUR CODE HERE ***"
    return all([sum_tree(b)== sum_tree(branches(t)[0]) for b in branches(t)])

def prune_tree(t, predicate):
    """
    Returns a new tree where any branch that has the predicate of the label
    of the branch returns True has its branches pruned.

    >>> prune_tree(tree(1, [tree(2)]), lambda x: x == 1) # prune at root
    [1]
    >>> prune_tree(tree(1, [tree(2)]), lambda x: x == 2) # prune at leaf
    [1, [2]]
    >>> prune_tree(test_tree, lambda x: x >= 3) # prune at 3, 4, and 5
    [1, [2, [4], [5]], [3]]
    >>> sum_tree(prune_tree(test_tree, lambda x: x > 10)) # prune nothing, add 1 to 9
    45
    >>> prune_tree(test_tree, lambda x: x > 10) == test_tree # prune nothing
    True
    """
    "*** YOUR CODE HERE ***"
    if predicate(label(t)):
        return tree(label(t))
    else:
        return tree(label(t), [prune_tree(b, predicate) for b in branches(t)])

# Q9. Closest
def closest(t):
    """ Return the smallest difference between an entry and the sum of the
    root entries of its branches .
    >>> t = tree(8 , [tree(4), tree(3)])
    >>> closest(t) # |8 - (4 + 3)| = 1
    1
    >>> closest(tree(5, [t])) # Same minimum as t
    1
    >>> closest(tree(10, [tree(2), t])) # |10 - (2 + 8)| = 0
    0
    >>> closest(tree(3)) # |3 - 0| = 3
    3
    >>> closest(tree(8, [tree(3, [tree(1, [tree(5)])])])) # 3 - 1 = 2
    2
    >>> sum([])
    0
    """
    diff = abs(label(t)- sum([label(b) for b in branches(t)]))
    return min([closest(b) for b in branches(t)]+[diff]) 

# Q10. Recursion
def dejavu(t, n):
    """
    >>> my_tree = tree(2, [tree(3, [tree(5), tree(7)]), tree(4)])
    >>> dejavu(my_tree, 12) # 2 -> 3 -> 7
    True
    >>> dejavu(my_tree, 5) # Sums of partial paths like 2 -> 3 don ’t count
    False
    """
    if is_leaf(t):
       return label(t)==n
    for b in branches(t):
        if dejavu(b, n-label(t)):
            return True
    return False

# Q11. Forest Path
def reduce(f, s, initial):
    """Combine elements of s pairwise
    using f, starting with initial.

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [2, 3, 1], 2)
    64
    """
    for x in s:
        initial = f(initial, x)
    return initial

# The one function defined below is used in the questions below 
# to convert truthy and falsy values into the numbers 1 and 0, respectively.
def one(b):
    if b:
        return 1
    else:
        return 0

def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    3
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    if is_leaf(t):
        return one(label(t)>=n)
    return sum([bigpath(b, n-label(t)) for b in branches(t)])

def allpath(t, f, g, s):
    """ Return the number of paths p in t for which f(reduce(g, p, s)) is truthy.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> even = lambda x: x % 2 == 0
    >>> allpath(t, even, max, 0) # Path maxes are 2, 4, and 5
    2
    >>> allpath(t, even, pow, 2) # E.g., pow(pow(2, 1), 2) is even
    3
    >>> allpath(t, even, pow, 1) # Raising 1 to any power is odd
    0
    """
    if is_leaf(t):
        return one(f(reduce(g, [label(t)], s)))
    return sum([allpath(b, f, g, g(s,label(t))) for b in branches(t)])

from operator import add , mul

def bigpath_allpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath_allpath(t, 3)
    3
    >>> bigpath_allpath(t, 6)
    2
    >>> bigpath_allpath(t, 9)
    1
    """
    return allpath(t, lambda x:x>=n, add, 0)
    
#################################################################################################
# TREE ADT:
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

