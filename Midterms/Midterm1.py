# Midterm1 Summer 2021

# Q4.Domain On the Range
# part(a)

def restrict_domain(f, low_d, high_d):
    """Returns a function that restricts the domain of F,
    a function that takes a single argument x.
    If x is not between LOW_D and HIGH_D (inclusive),
    it returns -Infinity, but otherwise returns F(x).
    >>> from math import sqrt
    >>> f = restrict_domain(sqrt, 1, 100)
    >>> f(25)
    5.0
    >>> f(-25)
    -inf
    >>> f(125)
    -inf
    >>> f(1)
    1.0
    >>> f(100)
    10.0
    """
    def restricted_f(x):
        if low_d <= x <= high_d:
            return  f(x)  
        return -float("inf")     
    return restricted_f

# part(b)
def restrict_range(f, low_r, high_r):
    """Returns a function that restricts the range of F, a function
    that takes a single argument X. If the return value of F(X)
    is not between LOW_R and HIGH_R (inclusive), it returns -Infinity,
    but otherwise returns F(X).
    >>> cube = lambda x: x * x * x
    >>> f = restrict_range(cube, 1, 1000)
    >>> f(1)
    1
    >>> f(-5)
    -inf
    >>> f(5)
    125
    >>> f(10)
    1000
    >>> f(11)
    -inf
    """
    def restricted_f(x):
        output = f(x)
        if low_r <= output <= high_r:
            return output
        return -float("inf")
    return restricted_f         

# par(c)    
def restrict_both(f, low_d, high_d, low_r, high_r):
    """
    Returns a version of F with a domain restricted to (LOW_D, HIGH_D)
    and a range restricted to (LOW_R, HIGH_R).
    >>> diva = lambda x: (10000 // x) * 9
    >>> f = restrict_both(diva, 1, 1000, 100, 999)
    >>> f(0)
    -inf
    >>> f(10000)
    -inf
    >>> f(200)
    450
    >>> f(100)
    900
    >>> f(1000)
    -inf
    """
    return restrict_range(restrict_domain(f, low_d, high_d), low_r, high_r)

# Q5. Digit Replacer
# part(a): Using iteration. 
def digit_replacer(predicate, transformer):
    """Returns a function that accepts a single number N (where N > 0) and
    returns a number where all digits that return true for PREDICATE(DIGIT)
    have been replaced by TRANSFORMER(DIGIT). TRANSFORMER is assumed to always
    return a valid digit >= 0 and <= 9.
    >>> is_even = lambda d: d % 2 == 0
    >>> lt_five = lambda d: d < 5
    >>> always_two = lambda d: 2
    >>> floor_divide_two = lambda d: d // 2
    >>> digit_replacer(is_even, floor_divide_two)(21098)
    11094
    >>> digit_replacer(lt_five, always_two)(1064592)
    2262592
    """    
    def replacer(n):
            if n<10:
                return transformer(n) if predicate(n) else n
            
            last, remaining = n%10, n//10
            number, digit_count = 0, 0 
            while remaining:
                if predicate(last):
                    number += transformer(last)*(10**digit_count)
                else:
                    number += last*(10**digit_count)
                last, remaining = remaining%10, remaining//10        
            return number
    return replacer    

# part(b): Using recursion.
def digit_replacer(predicate, transformer):
    """Returns a function that accepts a single number N (where N > 0) and
    returns a number where all digits that return true for PREDICATE(DIGIT)
    have been replaced by TRANSFORMER(DIGIT). TRANSFORMER is assumed to always
    return a valid digit >= 0 and <= 9.
    >>> is_even = lambda d: d % 2 == 0
    >>> lt_five = lambda d: d < 5
    >>> always_two = lambda d: 2
    >>> floor_divide_two = lambda d: d // 2
    >>> digit_replacer(is_even, floor_divide_two)(21098)
    11094
    >>> digit_replacer(lt_five, always_two)(1064592)
    2262592
    """    
    def replacer(n):
        if n<10:
            return transformer(n) if predicate(n) else n
        else:
            if predicate(n%10):
                return replacer(n//10)*10 + transformer(n%10)
            return replacer(n//10)*10 + n%10    
    return replacer    

# Q6. Run checker
def run_checker(condition, result):
    """
    Returns a chain function. Each call in a chain that starts with
    this returned function prints "No run!" if CONDITION returns a false
    value when applied to the previous two arguments and the current argument,
    and otherwise prints the result of applying RESULT to these same
    three arguments. For calls in the chain where there are fewer than two
    preceding calls in the chain, the missing arguments are taken to be -1.
    >>> f = run_checker(lambda a, b, c: a > b > c and a >= 10, lambda a, b, c: a*(b+c))
    >>> f = f(15)
    No run!
    >>> f = f(10)
    No run!
    >>> f = f(5)
    225
    >>> f = f(2)
    70
    >>> f = f(1)
    No run!
    >>> f = f(11)
    No run!
    >>> f = f(12)
    No run!
    >>> f = f(10)
    No run!
    >>> f = f(2)
    144
    """
    def f(a, b):
        def h(c):
            if condition(a,b,c):
                print(result(a,b,c))
            else:
                print("No run!")
            return f(b,c) 
        return h             
    return f(-1,-1)

# Q7. Measure twice, Cup once
def measure_methods(total_needed, cup_sizes):
    """Returns the number of ways to make exactly TOTAL_NEEDED with
    the given list of CUP_SIZES (sorted by smallest to largest).
    >>> measure_methods(128, [32, 64, 128])
    4
    >>> measure_methods(256, [32, 64, 128])
    9
    >>> measure_methods(384, [32, 64, 128])
    16
    >>> measure_methods(256, [16, 32, 64])
    25
    >>> measure_methods(125, [32, 64, 128])
    0
    """
    def helper_func(cup_size):
        """if total_needed%min(cup_sizes)!=0:
            return count
        if len(cup_sizes)==1:
            return 1 if total_needed%cup_sizes[0]==0 else count

        for e in cup_sizes:
            if total_needed%e!=0:
                pass
            else:
                count+= 1 + measure_methods(total_needed-e, cup_sizes[:cup_sizes.index(e)])
        return count"""
        count = 0
        if total_needed%cup_size==0:
            # using only one cup size
            count+=1 + helper_func(max([e for e in cup_sizes if e!=cup_size]))
        else:    
            # using cup_size in combo with lower cup_sizes
            while total_needed:
                if total_needed - cup_size=0:
                    pass
                else:
                    total_needed
    return helper_func(max(cup_sizes))    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
