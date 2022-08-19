# Discussion 3:

# Q1.Write a function that takes two numbers m and n and returns their product. 
# Assume m and n are positive integers. Use recursion, not mul or *! 
# Hint: 5 * 3 = 5 + (5 * 2) = 5 + 5 + (5 * 1).

def multiply(m ,n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if m==1:
        return n
    elif n==1:
        return m
    else:
        return m + multiply(m, n-1)

# Q3. Write a procedure merge(n1, n2) which takes numbers with digits in decreasing 
# order and returns a single number with all of the digits of the two, in decreasing 
# order. Any number merged with 0 will be that number (treat 0 as having no digits). 
# Use recursion.

# Hint: If you can figure out which number has the smallest digit out of both, then we 
# know that the resulting number will have that smallest digit, followed by the merge 
# of the two numbers with the smallest digit removed.

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    
    assert n1>=0 and n2>=0, "You can only merge positive numbers"
    
    # base case:
    if n1==0: 
        return n2
    elif n2==0: 
        return n1    
    if n1 < 10 and n2 < 10:
        return max(n1, n2)*10 + min(n1,n2)
    elif n1%10 > n2%10:
        return merge(n1, n2//10)*10 + n2%10
    else:
        return merge(n2, n1//10)*10 + n1%10


# Q4. Recursive Hailstone 
# Recall the hailstone function from Homework 1. First, pick a positive integer n as 
# the start. If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
# Repeat this process until n is 1. Write a recursive version of hailstone that prints
# out the values of the sequence and returns the number of steps.   

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    print(n)
    if n==1:
        return 1
    elif n%2 == 0:
        return hailstone(n//2) +1
    elif n%2 == 1:
        return hailstone(n*3 + 1) +1

# Q5: Is Prime
# Write a function is_prime that takes a single argument n and returns True if 
# n is a prime number and False otherwise. Assume n > 1 . We implemented this in
# Discussion 1 (/~cs61a/su21/disc/disc01/) iteratively, now time to do it recursively! 
# 

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    assert n>1, "n must be greater than 1!"
    
    def find_factor(factor):
        """This fubction checks whether a number is a factor (other than 1) 
        of the nonlocal variable N or not."""
        
        if factor == 1:
            return False
        elif n % factor == 0:
            return True
        else:
            return find_factor(factor-1)    

    # base case: n=2
    if n % (n-1) == 0:
        return True
    
    else:
        return False if find_factor(n//2) else True

# Q6. tree recursion
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n==0 or n==1:
        return 1
    else:
        return count_stair_ways(n-2) + count_stair_ways(n-1)

# Q7. Count K 
def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1 
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    
    if k==0 or k==1 :
        return 1
    elif k==2:
        return count_stair_ways(n)    
    elif n==k:
        return count_k(n, k-1) + (n-(k-1))
    elif n<k:
        return count_k(n,n)
    else:
        return sum([count_k(n-i,k) for i in range(1,k+1)])    

# Q8.'Tis it? 
def is_palindrome(s):
    """
    >>> is_palindrome("tenet")
    True
    >>> is_palindrome("tenets")
    False
    >>> is_palindrome("raincar")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    >>> is_palindrome("ab")
    False
    """
    if len(s)==1 or s=="":
        return True
    return is_palindrome(s[1:-1]) if s[0]==s[-1] else False

# Q9. Greatest pals
def greatest_pal(s):
    """
    >>> greatest_pal("tenet")
    'tenet'
    >>> greatest_pal("tenets")
    'tenet'
    >>> greatest_pal("stennet")
    'tennet'
    >>> greatest_pal("25 racecars")
    'racecar'
    >>> greatest_pal("abc")
    'a'
    >>> greatest_pal("")
    ''
    """
    if is_palindrome(s):
        return s
    left, right = s[0:-1], s[-1]
    i=0
    while i<len(left):
        if left[i] == right:
            return  greatest_pal(s[i:])
        i+=1
    return greatest_pal(left)

# Q10. Wait, It's All Palindromes?
def greatest_pal_two(s):
    """
    >>> greatest_pal_two("tenet")
    'tenet'
    >>> greatest_pal_two("tenets")
    'tenet'
    >>> greatest_pal_two("stennet")
    'tennet'
    >>> greatest_pal_two("abc")
    'a'
    >>> greatest_pal_two("")
    ''
    """
    for i in range(len(s)):
        if s[i]!=s[-i-1]:
            return greatest_pal_two(s[i+1:]) if s[i+1]==s[-1] and len(s)>2 else greatest_pal_two(s[i:-1]) 
    return s   

# Q11: All-Ys Has Been

Y = lambda f: (lambda x: x(x))(lambda x: f(lambda z: x(x)(z)))
fib_maker = lambda f: lambda r: 0 if r==0 else 1 if r==1 else fib_maker(lambda x:x)(r-1)+fib_maker(lambda x:x)(r-2)
is_pal_maker = lambda f: lambda r: r==r[::-1]

fib = Y(fib_maker)
is_pal = Y(is_pal_maker)

# This code sets up doctests for fib and is_pal. Run test(fib) and test(is_pal) to check your implementation

fib.__name__ = 'fib'
fib.__doc__="""Given n, returns the nth Fibonacci nuimber.

>>> fib(0)
0
>>> fib(1)
1
>>> fib(2)
1
>>> fib(3)
2
>>> fib(4)
3
>>> fib(5)
5
"""

is_pal.__name__ = 'is_pal'
is_pal.__doc__="""Returns whether or not an input string s is a palindrome.

>>> is_pal('tenet')
True
>>> is_pal('tenets')
False
>>> is_pal('ab')
False
>>> is_pal('')
True
>>> is_pal('a')
True
"""
