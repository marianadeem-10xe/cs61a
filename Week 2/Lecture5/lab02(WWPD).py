# Q2: Higher-order functions
def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

chocolate = cake()

more_chocolate, more_cake = chocolate(), cake

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y

cake = 'cake'  
#==================================
from operator import add, mul, mod

# Q#4 lambda_curry2()
def lambda_curry2(func):
    def adder(k):
        def addition(n):
            return n+k      
        return addition
    return adder    


curried_add = lambda_curry2(add)

add_three   = curried_add(3)

result      = add_three(5)  
#===================================
# Q#5 count_cond

def count_factors(n):
    """Return the number of positive factors that n has.
    >>> count_factors(6)
    4 # 1, 2, 3, 6
    >>> count_factors(4)
    3 # 1, 2, 4
    """
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count
print("###########\n")

lambda_count_fac = lambda n, i: n % i == 0
is_prime = lambda n, i: count_factors(i) == 2
print(count_factors(3), lambda_count_fac(3, 1) )
print(is_prime(5,2))