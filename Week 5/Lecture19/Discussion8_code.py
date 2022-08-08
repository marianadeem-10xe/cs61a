# Discussion 8
from math import prod


class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
         return self.x
    def __str__(self):
         return self.x * 2

class B:
    def __init__(self):
         print('boo!')
         self.a = []
    def add_a(self, a):
         self.a.append(a)
    def __repr__(self):
         print(len(self.a))
         ret = ''
         for a in self.a:
             ret += str(a)
         return ret

# Q3. Sum Nums
def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"         
    sum = 0
    while s.rest is not Link.empty:
        sum+=s.first
        s = s.rest
    return sum + s.first

# Q4. Multiply Lnks
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    """prod = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        prod *= link.first
    return Link(prod, multiply_lnks([link.rest for link in lst_of_lnks]))"""
    
    # For an extra challenge, try writing out an iterative approach as well below!
    "*** YOUR CODE HERE ***"
    """prod, prod_l = 1, Link.empty
    while all([bool(l) for l in lst_of_lnks]):  # list has True for empty link and Flase for non-empty links
        for i in range(len(lst_of_lnks)):
            if lst_of_lnks[i] is Link.empty:
                return Link.empty
            prod *= lst_of_lnks[i].first 
            lst_of_lnks[i]  = lst_of_lnks[i].rest
        prod_l += Link(prod)
        prod =1 
    prod_l+=Link(prod)       
    return prod_l"""
    def extend_link(s, t):
        if s is Link.empty:
            return t
        else:
            return Link(s.first, extend_link(s.rest, t)) 

    prod = 1
    m = min([len(link) for link in lst_of_lnks])
    for i in range(m):
        for link in lst_of_lnks:
            prod *= link[i]
        if i==0:
            prod_link = Link(prod)
        else:    
            prod_link = extend_link(prod_link, Link(prod))
        prod = 1        
    return prod_link       

# Q5. Flip_two
def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    "*** YOUR CODE HERE ***"
    # recursive approach
    """def helper(s,count=0):
        l = s
        
        if len(s)<2:
            return 

        for _ in range(count):
            l = l.rest.rest
        
        if not (l is Link.empty or l.rest is Link.empty):
            temp = l.first
            l.first = l.rest.first
            l.rest.first = temp
            helper(s, count+1)
    
    return helper(s)"""        
    
    # For an extra challenge, try writing out an iterative approach as well below!
    "*** YOUR CODE HERE ***"
    
    # iterative approach
    if len(s)<2:
        return
    l     = s
    count = 0
    while True:
        for _ in range(count):
            l = l.rest.rest
        if not (l is Link.empty or l.rest is Link.empty):
            temp = l.first
            l.first = l.rest.first
            l.rest.first = temp
            count+=1
            l=s
        else:
            return  
            
# Q6. Make even
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    "*** YOUR CODE HERE ***"
    if t.label%2==1:
        t.label+=1
    for b in t.branches:
        make_even(b)    

# Q7. Leaves
def leaves(t):
    """Returns a list of all the labels of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"            
    lst = []
    if t.is_leaf():
        lst.append(t.label)
    for b in t.branches:
        lst+=leaves(b)
    return lst    

# Q8. Find paths   
def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """

    paths = []
    if t.label==entry:
        paths.append([t.label])
    for b in t.branches:
        paths.extend([t.label]+path for path in find_paths(b, entry) if path[-1]==entry)
    return paths   

# Exam Prep
# Q9. Node Printer
def node_printer(t):
    """
    >>> t1 = Tree(1, [Tree(2,
    ...                   [Tree(5),
    ...                    Tree(6, [Tree(8)])]),
    ...               Tree(3),
    ...               Tree(4, [Tree(7)])])
    >>> printer = node_printer(t1)
    >>> for _ in range(8): # NOTE: it's okay to fail this test if all 8 are printed once
    ...     printer()
    1
    2
    3
    4
    5
    6
    7
    8
    """
    to_explore = [t]
    def step(count=0):
        node = [print(tree.label) for tree in to_explore]
        [print(n) for n in node]
        yield
        to_explore = [b for b in [tree.branches for tree in to_explore]]
        step()
    return step
    
# Q10: Iterator Tree Link Tree Iterator
# Part A
def funcs(link):
    """
    >>> t = Tree(1, [Tree(2,
    ...                   [Tree(5),
    ...                    Tree(6, [Tree(8)])]),
    ...               Tree(3),
    ...               Tree(4, [Tree(7)])])
    >>> print(t)
    1
      2
        5
        6
          8
      3
      4
        7
    >>> func_generator = funcs(Link.empty) # get root label
    >>> f1 = next(func_generator) 
    >>> f1(t)
    1
    >>> func_generator = funcs(Link(2)) # get label of third branch
    >>> f1 = next(func_generator)
    >>> f2 = next(func_generator)
    >>> f2(f1(t))
    4
    >>> # This just puts the 4 values from the iterable into f1, f2, f3, f4
    >>> f1, f2, f3, f4 = funcs(Link(0, Link(1, Link(0))))
    >>> f4(f3(f2(f1(t))))
    8
    """
    if link is Link.empty:
        yield lambda t: t.label
    else:
        yield lambda t : t.branches[link.first]
        yield from funcs(link.rest)

# Paart B
def apply(g, t, link):
    """
    >>> t = Tree(1, [Tree(2,
    ...                   [Tree(5),
    ...                    Tree(6, [Tree(8)])]),
    ...               Tree(3),
    ...               Tree(4, [Tree(7)])])
    >>> print(t)
    1
      2
        5
        6
          8
      3
      4
        7
    >>> apply(lambda x: x, t, Link.empty) # root label
    1
    >>> apply(lambda x: x, t, Link(0))    # label at first branch
    2
    >>> apply(lambda x: x * x, t, Link(0, Link(1, Link(0))))
    64
    """
    for f in funcs(link):
        t = f(t)
    return g(t)    

# Q11: O!-Pascal - Fall 2017 Final Q4
# Part (a)
def pascal_row(s):
    """
    >>> a = Link.empty
    >>> for _ in range(5):
    ...     a = pascal_row(a)
    ...     print(a)
    <1>
    <1 1>
    <1 2 1>
    <1 3 3 1>
    <1 4 6 4 1>
    """
    if s is Link.empty:
        return Link(1)
    start = Link(1)
    last, current = start, s
    while not current.rest is Link.empty:
        last.rest = Link(current.first+current.rest.first)
        last , current = last.rest, current.rest
    last.rest = Link(current.first)
    return start

# Part (b)
def make_pascal_triangle(k):
    """
    >>> print(make_pascal_triangle(5))
    <<1> <1 1> <1 2 1> <1 3 3 1> <1 4 6 4 1>>
    """
    if k == 0:
        return Link.empty
    row = Link(1)
    end = Link(row)
    result = end
    for _ in range(k-1):
        row = pascal_row(end.first)
        end.rest = Link(row)
        end = end.rest
    return result

# Part (c)
def diagonal(tri, n):
    """
    >>> triangle = make_pascal_triangle(6)
    >>> print(diagonal(triangle, 1))
    <1 1 1 1 1 1>
    >>> print(diagonal(triangle, 2))
    <1 2 3 4 5>
    >>> print(diagonal(triangle, 3))
    <1 3 6 10>
    """
    if tri is Link.empty:
        end = Link.empty
    else:
        p, j = tri.first, 1
        while j<n and p.rest:
            p,j = p.rest, j+1
        if j==n:
            end = Link(p.first, diagonal(tri.rest, n))
        else:
            end = diagonal(tri.rest, n)
    return end


#####################################################################################
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
    # added functions 
    #######################
    # __getitem__ is not allowed to use (for Q11).
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    
    def __len__(self):
        return 1 + len(self.rest)


  
    #######################
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()