# Author: Paul Quaife
# Date: 1/19/2021
# Description: Asks for numbers, then lists the min and max.

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
