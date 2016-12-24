"""
n! means n*(n-1)x....
For example, 10! = 10x9x8x7x6x5x4x3x2x1 = 3628800
sum the digits in the number 10! is 3+6+2+8+8+0+0 = 27


Find the sum of the digits in the number 100!
Ryan Gordon -

"""
# Standard factorial function
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1) # Recursively call fact until we have gone through all facts



factNum = fact(100) # Calls the fact function, number given is the factorial
# from one of my other solutions. Split the int into singular digits in a list
# we then call sum on this list
print sum([int(i) for i in str(factNum)])
