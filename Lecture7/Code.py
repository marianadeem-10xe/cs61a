# Mutual recursion
def is_even(n):
     return n % 2 == 0
def play_alice(n):
     if n == 0:
          print("Bob wins!")
     else:
          play_bob(n-1)
def play_bob(n):
     if n == 0:
          print("Alice wins!")
     elif is_even(n):
          play_alice(n-2)
     else:
          play_alice(n-1)

#play_alice(20)

# Lab03: Recursion

# Q1. WWPD
def f(a, b):
     if a > b:
         return f(a - 3, 2 * b)
     elif a < b:
         return f(b // 2, a)
     else:
         return b

"""f(2, 2)
f(7, 4)
f(2, 28)
f(-1, -3)"""

# Q2. WWPD

def crust():
     print("70km")
     def mantle():
          print("2900km")
          def core():
               print("5300km")
               return mantle()
          return core
     return mantle

