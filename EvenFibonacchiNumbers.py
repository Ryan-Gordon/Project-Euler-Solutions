"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Ryan Gordon
"""


a = int(raw_input('Enter number of terms for this fib sequence. NOTE: at least 34 required to get up to 4 Million : '))

def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        if ((a % 2 ==0) and( a < 4000000)):

            yield a
            print(str(a)+" is an even fibonacci number and is the "+str(_)+" term in the Fibonacci sequence")
        a, b = b, a + b

print("The sum of all even Fibonacci numbers is "+str(sum(list(fib(a)))))

