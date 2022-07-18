def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(lst)):
        lst[i] = fn(lst[i])

def swap(a, b):
    """Swap the contents of lists a and b.

    >>> a = [1, 'two', 3]
    >>> b = [4, [5, 6]]
    >>> swap(a, b)
    >>> a
    [4, [5, 6]]
    >>> b
    [1, 'two', 3]
    """
    "*** YOUR CODE HERE ***"
    a.extend(b)
    org_a = a[:len(a)-len(b)]
    b[:] = org_a 
    for e in org_a:
        a.remove(e)

def lgk_pow(n, k):
    """Computes n^k.

    >>> lgk_pow(2, 3)
    8
    >>> lgk_pow(4, 2)
    16
    >>> a = lgk_pow(2, 100000000) # make sure you have log time
    """
    "*** YOUR CODE HERE ***"
    
    """if k is an even number, the input n is squared first and then raised to the exponent k.
    This reduces the the number of iterations to be executed."""
    
    if k == 1:
        return n
    elif k == 0:
        return 1    
    for i in range(k):
        if k%2 == 0:
            return lgk_pow(n*n, k//2)
        else:
            return lgk_pow(n*n, k//2)*n    

from math import sqrt


def is_prime_sqrt(n):
    """Tests whether a number N is prime or not. Implement this function
    in O(sqrt(n)) time. You can assume n >= 2

    >>> is_prime_sqrt(2)
    True
    >>> is_prime_sqrt(67092481)
    False
    >>> is_prime_sqrt(524287)
    True
    >>> is_prime_sqrt(2251748274470911)
    False
    >>> is_prime_sqrt(6700417)
    True
    >>> is_prime_sqrt(44895587973889)
    False
    >>> is_prime_sqrt(2147483647)
    True
    >>> is_prime_sqrt(67280421310721)
    True
    """
    # sqrt(k) will give the square root of k as a floating point (decimal)
    "*** YOUR CODE HERE ***"
    sq_n = sqrt(n)

    if int(sq_n)*int(sq_n) == n:
        return False
    else:
        for i in range(2, int(sqrt(n))):
            if n%i==0:
                return False
        return True    