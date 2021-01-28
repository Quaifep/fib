# Author: Paul Quaife
# Date: 1/27/2021
# Description: Fib Sequence

def fib(n):
    """Takes a positive integer and returns the number at that position of the Fibonacci sequence."""
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
