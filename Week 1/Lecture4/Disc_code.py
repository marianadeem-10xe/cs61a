# Q#1: Jacket Weather
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    return True if temp<60 or raining else False

#Q3: Square so slow
def square(x):
    print("here!")
    return x * x
def so_slow(num):
    x = num
    while x > 0:
        x=x+1
    return x / 0
#square(so_slow(5))            

#Q4: Is prime
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    
    assert n>1, "Input must be greater than 1!!"
    factor = 2
    while factor < n:
        if n%factor == 0:
            return False
        factor+=1    
    return True 

#Q5: Fizzbuzzz   
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    "*** YOUR CODE HERE ***"
    a = 1
    while a<=n:
        if a%3 ==0 and a%5 ==0: 
            print("fizzbuzz")
        elif a%3==0:
            print("fizz")
        elif a%5==0:
            print("buzz") 
        else:
            print(a)
        a+=1    
        