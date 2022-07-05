# Lecture 6
# Split positive n into all but its last digit and its last digit

def split(n):
    return n//10, n%10

def sum_digits(n):
    if n<10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last, last)

# Recursion vs iterations: 
def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total         

def fact_rec(n):
    if n==0:
        return 1
    else:
        return n*recursive_fact(n-1)  

# Mutual recursion           
# When a recursive procedure is divided among two functions that call each other, the functions are
# said to be mutually recursive

# Luhn sum
# Starting from the leftmost digit (units digit, it is also called the check digit), moving left, double every second digit
# if the result is greater than 9, then sum the digits, lastly: add all digits.

def sum_digits(n):
    if n < 10:
        return n
    else:
        last = n % 10
        all_but_last = n // 10
        return last + sum_digits(all_but_last)

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last    

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return  luhn_sum(all_but_last) + luhn_digit

#print(luhn_sum(125256))           

# Cascade
def cascade(n):
    """Print a cascade of prefixes of n."""
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)
def inverse_cascade(n):
    """">>>inverse_cascade(1234)
    1       # first three lines are coming from the grow func and the last three lines are from the shrink function.
    12
    123
    1234
    123
    12
    1

    """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow   = lambda n: f_then_g(grow, print , n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)  

inverse_cascade(1234)