"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1
The 12th term , F12 is the first term to contain three digits
What is the index of the first term in the Fibonacci Squence to contain 1000 digits.
Ryan Gordon
"""

def fib():
    a, b = 0, 1
    terms=1 # Used to iterate over each term.
    foundFib = False
    while(foundFib == False):

        # Cast number to String, get length of number and if it is 1000 in length we found our fib number
        if (len(str(a)) == 1000):
            print "Found answer. At term %d, found a number with 1000 digits. \n Index is %d \n Number is %d" % (terms,terms-1,a)
            foundFib = True # Not really needed because we use return but good manners
            return a
        a, b = b, a + b # Do fib calculation
        terms += 1

fib()

