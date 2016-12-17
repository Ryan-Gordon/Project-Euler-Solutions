"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?


Can be done in 1 line.
Solution:
We want to get the result of 2 to power of 1000
We then want to get all the numbers in the result indivdually
To finish we sum these single digits
"""
print sum([int(i) for i in str(2**1000) ])


num = int(raw_input("Input number:"))

power = int(raw_input("Input power:"))

print "Number we want to sum is %s to power of %s" % (num,power)
print sum([int(i) for i in str(num**power) ])
