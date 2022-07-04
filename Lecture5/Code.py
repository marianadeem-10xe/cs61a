# Codes discussed in Lecture5 
# How to create an environment diagram:
# when a function is defined: create a function value:- 
# current frame: current frame name func <name>(<params>) [parent=current frame]

def make_adder(n):              
    def adder(k):               # f1: make_adder func adder(k) [parent=f1]  
        return k+n    
    return adder
add_3 = make_adder(3)
#print(add_3(5))    
#print(add_3(89))    

# Local names:
# Function parameters have a local scope meaning that they can only be accessed within the current frame.

"""def f(x,y):
    return g(x)
def g(a):
    return a+y      # this line will produce error as y is not defined within the env of g(global frame and the f1:g frame). 
result = f(1,2)"""

# Function composition:
def square(x):
    return x*x

def triple(x):
    return 3*x  

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h          
squiple = compose1(square, triple)          
result  = squiple(4)

# Self reference:
def print_all(x):
    print(x)
    return print_all
#a = print_all(1)(20)(5)     # the function can be called as many times as one wants as it returns itself

# Currying:
# a function which transforms a multi-argument function to a single-argument function
 
def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g 

def uncurry(g):
    def f(x,y):
        return g(x)(y)
    return f    

from operator import add 
add_x = curry2(add)(5)          # curry2 appplied on add would create an adder function that can add 5 to any number.  
print(curry2(add)(5)(6))        # adder is applied to 6 to add 5 and 6. 

curried_add = curry2(add)
uncurried_add = uncurry(curried_add)   # transforms the single-argument function back to multi-argumnet function.

print(uncurried_add(4,5))

# implimenting funstions
# write a function that takes a number 'n' as input and returns this number afer ommiting the given digit.

def remove(n, digit):
    """>>> remove(231,3)
    21
    remove(243132,2)
    4313"""
    kept, digits = 0,0
    while n!=0:
        n, last = n//10, n%10
        if last != digit:
            kept = kept + last**10
            digits +=1
    return kept           