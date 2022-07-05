# Date: 20-6-22
#===============================================================================
# Chapter 1: 1.2
#===============================================================================
# Premitive (P) and Compound Expressions (CE)
# Numbers
P  = 42
CE = 1/2 + 1/4 + 1/8 + 1/16 + 1/32 + 1/64 + 1/128

# Call expression
maximum_val = max(7.5,9.65)     # comprises of operator and operand
exp_2       = pow(100,2)        # order of the operands matter
exp_100     = pow(2,100)

# Nested Expressions (NE)
NE = max(min(1, -2), min(pow(3, 5), -4))

# Python Liberaries
# math module provides a variety of familiar mathematical functions.
from math import sqrt
x2 = sqrt(234)

# operator module provides access to functions corresponding to infix operators.
from operator import add, sub, mul
op = add(14, 28)
op = sub(100, mul(7, add(8, 4)))

# Assignment Statements
radius   = 10
diameter = 2* radius

# Function and variable names are also bound via import statements e.g. pi
# but can be renamed
from math import pi
pi_ = pi*71/223

from math import pi as k
k_  = k*71/223              # value stored in pi_ and k_ is the same

f   = max
output_f = max(7.5,9.5)     # value stored in maximum_val and output_f is the statements

# Successive Assignment Statements (SAS)
# Assigns a new value/overwrites the value stored in a previously defined variable.
f   = 2

# Multiple assignments in single statement
area, circumference = pi*radius**2, 2*pi*radius

#===============================================================================
# Chapter 1: 1.3
#===============================================================================
# Functions
def square(x):      # def <function name>(<formal parameters>)
    return x*x
