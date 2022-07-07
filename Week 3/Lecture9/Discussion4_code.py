# Discussion 4

# Q2. Even weighted
# Write a function that takes a list s and returns a new list that keeps only the 
# even-indexed elements of s and multiplies them by their corresponding index. 

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i]*i for i in range(0,len(s),2) if i%2==0]

# Q3: Closest Number:
# Write a function that takes in a list of numbers nums and a target number target and 
# returns the number in nums that is the closest to target . If there's a tie, return 
# the number that shows up earlier in the list. You should do this in one line.

# Hint: To find how close two numbers are, you can use abs(x - y) Hint 2: Use the min 
# function and pass in a key function.    

def closest_number(nums, target):
    """
    >>> closest_number([1, 4, 5, 6, 7], 2)
    1
    >>> closest_number([3, 1, 5, 6, 13], 4) #  choose the earlier number since there's a tie
    3
    >>> closest_number([34, 102, 8, 5, 23], 25)
    23
    """
    def min_distance(list, target):
        min_dist =  min([abs(x-target) for x in nums])
        return min_dist
   
    return min([x for x in nums if abs(x-target)==min_distance(nums, target)])   

# Q4: Max Product
# Write a function that takes in a list and returns the maximum product that can be formed
# using nonconsecutive elements of the list. The input list will contain only numbers greater 
# than or equal to 1.    

def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    def reduce(reduced_fn, s , initial):
        reduced = initial
        for e in s:
            reduced = reduced_fn(reduced, e)
        return reduced

    if len(s)==0:
        return 1
    elif len(s)==3:
        products = [max(s[0]*s[2], s[1])]
            
    else:
        products = []
        for i in range(len(s)):
            elements = [s[i]] + [elem for elem in s if abs(i-s.index(elem))>1]
            print(elements)
            # products += elements
        print(products)    
print(max_product([1,9,2]))                       

# Q6. Group By

def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for i in range(len(s)):
        values  = [s[i]]
        key = fn(s[i])
        if key in grouped.keys():
            continue
        else:
            for e in s[i+1:]:
                if fn(e)==key:
                    values += [e]
            grouped[key] = values 
    
    return grouped

# Q7: Subset Sum (from Su15 MT 1):

def subset_sum(target, lst):
    """Returns True if it is possible to add some of the integers in lst
    to get target.

    >>> subset_sum(10, [-1, 5, 4, 6])
    True
    >>> subset_sum(4, [5, -2, 12])
    False
    >>> subset_sum(-3, [5, -2, 2, -2, 1])
    True
    >>> subset_sum(0, [-1, -3, 15])     # Sum up none of the numbers to get 0
    True
    """
    if target==0 or target in lst:
        return True
    elif target not in lst and len(lst)==1:
        return False
    else:
        a = target in lst
        b = 0 #for len range(2, len(lst))
        return a or b

# Q8: Intersection (from Su15 MT 1)
def intersection(lst_of_lsts):
    """Returns a list of distinct elements that appear in every list in
    lst_of_lsts.

    >>> lsts1 = [[1, 2, 3], [1, 3, 5]]
    >>> intersection(lsts1)
    [1, 3]
    >>> lsts2 = [[1, 4, 2, 6], [7, 2, 4], [4, 4]]
    >>> intersection(lsts2)
    [4]
    >>> lsts3 = [[1, 2, 3], [4, 5], [7, 8, 9, 10]]
    >>> intersection(lsts3)         # No number appears in all lists
    []
    >>> lsts4 = [[3, 3], [1, 2, 3, 3], [3, 4, 3, 5]]
    >>> intersection(lsts4)         # Return list of distinct elements
    [3]
    """
    elements = []
    for e in sum(lst_of_lsts, []):
        condition = False
        if e not in elements:
            condition = all([e in lst for lst in lst_of_lsts] )
        if condition:
            elements = elements + [e] 
    return elements

# Q9: Wordify (from Sp17 Mock Midterm 1)
def wordify(s):
    """ Takes a string s and divides it into a list of words. Assume that the last element of the string is a whitespace.
    Duplicate words allowed.
    >>> wordify ('sum total of human knowledge ')
    ['sum', 'total', 'of', 'human', 'knowledge']
    >>> wordify ('one should never use exclamation points in writing! ')
    ['one', 'should', 'never', 'use', 'exclamation', 'points', 'in', 'writing!']
    """

    start, end, lst = 0,0,[]
    for letter in s:
        if letter!= " ":
            end+=1
        else:
            lst+= [s[start:end]]
            start, end = end+1, end+1 
    return lst           