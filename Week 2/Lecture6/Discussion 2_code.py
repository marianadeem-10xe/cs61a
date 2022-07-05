# Discussion 2

# Q1.Write a function that takes in a function cond and a number n 
# and prints numbers from 1 to n where calling cond on that number returns True .

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i<=n:
        if cond(i):
            print(i)
        i+=1    
            
# Q2. Write a function similar to keep_ints like in Question 1, but now it takes 
# in a number n and returns a function that has one parameter cond. The returned 
# function prints out numbers from 1 to n where calling cond on that number returns True.
# 

def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 
    1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    def print_int(cond):
        i = 1
        while i<=n:
            if cond(i):
                print(i)
            i += 1    

    return print_int  

# Q4. Curry2 Lambda
# Write curry2 as a lambda function.

# Q5. Environment diagram
n = 7
def f(x):
    n = 8
    return x + 1
def g(x):
    n = 9
    def h():
        return x + 1
    return h
def f(f, x):
    return f(x + n)
f = f(g, n)
g = (lambda y: y())(f)

# Q6.The function make_keeper_redux is similar to make_keeper , but now the function 
# returned by make_keeper_redux should be self-referential—i.e., the returned function
# should return a function with the same behavior as make_keeper_redux.
# Hint: you only need to add one line to your make_keeper solution.

def make_keeper_redux(n):
    """Returns a function. This function takes one parameter <cond> and prints out
    all integers 1..i..n where calling cond(i) returns True. The returned
    function returns another function with the exact same behavior.
    >>> def multiple_of_4(x):
    ...     return x % 4 == 0
    >>> def ends_with_1(x):
    ...     return x % 10 == 1            
    >>> k = make_keeper_redux(11)(multiple_of_4)
    4
    8
    >>> k = k(ends_with_1)
    1
    11"""
    
    "*** YOUR CODE HERE ***"
    def print_int(cond):
        i = 1
        while i<=n:
            if cond(i):
                print(i)
            i += 1    
        return print_int        # added line in make_keeper function
    return print_int

# Q7. Write a function print_delayed that delays printing its argument until the 
# next function call. print_delayed takes in an argument x and returns a new function
# delay_print. When delay_print is called, it prints out x and returns another delay_print. 

def print_delayed(x):
    """Return a new function. This new function, when called, will print out x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi") # a function is returned
    5
    <function delay_print>"""
    def delay_print(y):
        nonlocal x
        print(x)
        x = y     
        return delay_print
    return delay_print

# Q8. Write a function print_n that can take in an integer n and returns a repeatable 
# print function that can print the next n parameters. After the nth parameter, 
# it just prints "done".

def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    
    def inner_print(x):
        nonlocal n
        if not n:
            print("done")
        else:
            print(x)
            n-=1

        return inner_print
    return inner_print
