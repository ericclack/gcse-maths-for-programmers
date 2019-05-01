import math

def e_seq(n):
    "Sum sequence of 1 / i! for i = 0 ... n"
    if n == 0: return 1
    else: return 1 / math.factorial(n) + e_seq(n-1)

def h_seq(n):
    "Sum sequence of 1 / 2^i for i = 1 ... n"
    if n == 1: return 1/2
    else: return (1 / (2 ** n)) + h_seq(n-1)
    
def fib(n):
    if n == 1: return 1
    elif n == 2: return 1
    else: return fib(n-1) + fib(n-2)
    

def show_seq(fn, n):
    print("fn applied to range 1 ...", n)
    for i in range(1,n):
        print(fn(i), end=", ")
        
              
