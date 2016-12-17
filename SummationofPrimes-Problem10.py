summation = 0
i = 1
n = 2000000
primeCount = 0

# function to factor a given positive integer n
def is_prime(n):
    # look for factors of 2 first
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
while(i<n):
    if(is_prime(i)):
        summation = summation + i
        primeCount += 1
        print i

    i += 1

print primeCount
print summation
# Answer is 142913828922
