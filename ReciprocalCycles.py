"""
Problem 28 Reciprocal Cycles

Find the value of d < 1000 for which
1/d contains the longest recurring cycle
in its decimal fraction part.

In my attempts to solve this problem, I stumbled upon a maths concept known as Prime Sieves.

"""


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n//2) if sieve[i]]


# Project Euler Problem 26

def f(L):
    if L < 8: return 3
    for d in prime_sieve(L)[::-1]:
        period = 1
        while pow(10, period, d) != 1: period += 1
        if d - 1 == period: break
    return d


L = int(input('The longest recurring cycle for 1/d where d < '))
print "is", f(L)