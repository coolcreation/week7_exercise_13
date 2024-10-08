#!/usr/bin/env python3
#  Jeff Bohn
#  10/1/2024
#  Recursion and Algorithms
#  Chapter 13

############ Exercise 13-1 ############

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    n1 = 0
    n2 = 1
    fib = 0
    for i in range(2, n+1):
        fib = n1 + n2
        n1 = n2
        n2 = fib
    return fib

def main():
    for i in range(100):
        print(fib(i), end=", ")
    print("...")


main()
