# Author: Paul Quaife
# Date: 1/27/2021
# Description: Fib Sequence

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
