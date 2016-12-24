"""
2520 is the smallest number that can be divided by each of the numbers 1 to 10
What is the smallest positive number that is evenly divisble by all of the numbers



Ryan Gordon

Solution:
Given we want the smallest number we should start with a low number work our way up
First number we find will be the smallest number

We want to iterable numbers starting at 20
And check if divisible by 20, if divisible by 19...

"""



"""

This is an incredibly dirty solution
Will try to implement something a bit smarter at a later point
Log(n) in best case
Only 1 number between 1 - 232792560 can be divided by 20-10
This same number is our smallest multiple of all numbers between 1 and 20

"""
import time # This is used simply to show the speed of the solution

startTime = time.time() # Get current time
n = 20
while (n< 2000000000000000):
    if(n % 20 == 0):
        if (n % 19 == 0):
            if (n % 18 == 0):
                if (n % 17 == 0):
                    if (n % 16 == 0):
                        if (n % 15 == 0):
                            if (n % 14 == 0):
                                if (n % 13 == 0):
                                    if (n % 12 == 0):
                                        if (n % 11 == 0):
                                            if (n % 10 == 0):
                                                print"Passed first 10 conditions with : " + str(n)
                                                if (n % 9 == 0):
                                                    if (n % 8 == 0):
                                                        if (n % 7 == 0):
                                                            if (n % 6 == 0):
                                                                if (n % 5 == 0):
                                                                    if (n % 4 == 0):
                                                                        if (n % 3 == 0):
                                                                            if (n % 2 == 0):
                                                                                if (n % 1 == 0):
                                                                                    print("Found smallest multiple : "+str(n) )
                                                                                    break


    n += 1 # Add to n and check next number




elapsedTime = (time.time() - startTime) # Check how long it has been since program start
print "Elapsed time  %d" % (elapsedTime)