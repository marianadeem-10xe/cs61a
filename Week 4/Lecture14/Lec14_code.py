# Lecture14
t = tree(1, [tree(2, [tree(3), tree(4)]), tree(5, [tree(6, [tree(7, [tree(8)])])])])

print_tree(t)
draw(t)

def max_tree(t):
    """
    >>> max_tree(t)
    8
    >>> max_tree(tree(9, [t]))
    9
    """
    if is_leaf(t):
        return label(t)
    # value at current nodes   max of each branch
    return max([label(t)] + [max_tree(b) for b in branches(t)])
    
def sum_tree(t):
    """
    >>> sum_tree(t) == 1+2+3+4+5+6+7+8
    True
    """
    if is_leaf(t):
        return label(t)
    return sum([label(t)] + [sum_tree(b) for b in branches(t)])
    
def num_nodes(t):
    """
    >>> num_nodes(t)
    8
    """
    if is_leaf(t):
        return 1
    result = 0
    for b in branches(t):
        result = result + num_nodes(b)
    return result + 1
    
def num_leaves(t):
    """
    >>> num_leaves(t)
    3
    """
    if is_leaf(t):
        return 1
    result = 0
    for b in branches(t):
        result = result + num_leaves(b)
    return result

def odd_row_sum(t):
    """
    >>> odd_row_sum(t)
    22
    """
    if is_leaf(t):
        return label(t)
    result = label(t)
    # branches(branches(t))? Nope, branches(t) returns a list,
    # branches takes in a tree, not a list
    for b in branches(t):
        # calling odd_row_sum(b) is WRONG 
        # skip over the even row nodes
        for d in branches(b):
            result = result + odd_row_sum(d)
    return result
    
def even_row_sum(t):
    """
    >>> even_row_sum(t)
    14
    """
    if is_leaf(t):
        return 0
    result = 0
    for b in branches(t):
        result = result + label(b)
        for d in branches(b):
            result = result + even_row_sum(d)
    return result

def labels(t):
    """List all tree expressions for tree t.
    >>> t = tree(3, [tree(4, [tree(-1)]), tree(-5)])
    >>> for e in labels(t):
    ...     print(e)
    label(t)
    label(branches(t)[0])
    label(branches(branches(t)[0])[0])
    label(branches(t)[1])
    """
    def traverse(t, e):
        result.append("label(" + e + ")")
        for i in range(len(branches(t))):
            traverse(branches(t)[i], "branches(" + e + ")[" + str(i) + "]")
    result = []
    traverse(t, 't')
    return result

def factorial_tree(n):
    if n == 0:
        return tree(1)
    bs = [factorial_tree(n-1)]
    return tree(n * label(bs[0]), bs)
    
def factor_tree(n):
    for i in range(2, n):
        if n % i == 0:
            return tree(n, [ factor_tree(n // i), factor_tree(i)])
    return tree(n)
    
def apply_tree(fn_tree, val_tree):
    """ Creates a new tree by applying each function stored in fn_tree
    to the corresponding labels in val_tree
    >>> double = lambda x: x*2
    >>> square = lambda x: x**2
    >>> identity = lambda x: x
    >>> t1 = tree(double, [tree(square), tree(identity)])
    >>> t2 = tree(6, [tree(2), tree(10)])
    >>> t3 = apply_tree(t1, t2)
    >>> print_tree(t3)
    12
      4
      10
    """                 # Function call
    f = label(fn_tree)
    new_label = f( label(val_tree) )
    # print(new_label)
    bs = []
    for i in range(len(branches(fn_tree))):
        bs.append(apply_tree(branches(fn_tree)[i], branches(val_tree)[i]))
    return tree(new_label, bs)

def is_combo(n, k): 
    """ Is k a combo of n? A combo of a non-negative integer n 
    is the result of adding or multiplying the digits of n 
    from left to right, starting with 0  
    >>> [k for k in range(1000) if is_combo(357, k)] 
    [0, 7, 12, 15, 22, 35, 56, 105]
    """
    # is_combo(357, 35)
    # is_combo(35, 35 // 7) 
    # is_combo(35, 5)
    # ((0 + 3) + 5) * 7 == 56
    assert n >= 0 and k >= 0 
    # if n is 0, great, if not, multiply the leftover digits by 0 and add that
    if k == 0: 
        return True 
    if n == 0: 
        return False 
    rest, last = n // 10, n % 10 
                            # subtracting a number is adding an addition to the end
    added = k - last >= 0 and is_combo(rest, k - last) 
                            # diving a number is adding a multiplication to the end
    multiplied = k % last == 0 and is_combo(rest, k // last) 
    return added or multiplied

def make_checker_tree(t, so_far=0):
    """ Returns a function tree that, when applied to another tree, 
    will create a new tree where labels are True if the label is a combination 
    of the path in t from the root to its corresponding node.
    >>> t1 = tree(5, [tree(2), tree(1)])
    >>> fn_tree = make_checker_tree(t1)
    >>> t2 = tree(5, [tree(10), tree(7)])
    >>> t3 = apply_tree(fn_tree, t2) #5 is a combo of 5, 10 is a combo of 52, 7 isn't a combo of 51
    >>> print_tree(t3)
    True
      True
      False
    """
    # 5
    # \
    # 2 
    # turns into 52
    new_path = so_far * 10 + label(t)
    branches = [make_checker_tree(b, new_path) for b in branches(t)]
    fn = lambda x: is_combo(new_path, x)
    return tree(fn, branches)

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
