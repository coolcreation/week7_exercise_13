#!/usr/bin/env python3
#  Jeff Bohn
#  10/1/2024
#  Recursion and Algorithms
#  Chapter 13

############ Exercise 13-1 ############

import traceback

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    for i in range(100):
        print(fib(i), end=", ")
    print("...")
    #traceback.print_exc()

main()








# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)

# def main():
#     for i in range(16):
#         print(fib(i), end=", ")
#     print("...")

# if __name__ == "__main__":
#     main()
