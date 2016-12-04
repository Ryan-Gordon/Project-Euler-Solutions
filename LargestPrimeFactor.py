"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Solution complexity : Log(n)

"""
# Used for iteration over the loop. This is log(n)
i = 1

# Test value is 13195, first primes should be 5,7,13,29
# Problem number is 600851475143, first primes are 71, 839,1471
n = 600851475143
primeFactors = []

while(i<n):
    if(i%i ==0 and i%1 == 0):
        #If we enter here it means we have a prime number
        # Now check for factor of n
        if(n % i == 0):
            print(str(i) + " is a prime factor of "+str(n))
            primeFactors.append(i)
            # Solution! To stop checking all values  we use reduce to multiply all elements in the list
            # If the result is n then we found the number
            sum = reduce(lambda x, y: x * y, primeFactors)


        if(sum == n):
            break

        i += 1

# Possible ways to reduce run time
# Add primeFactors(  len(primeFactors) - 1) to i as there will be no more factors before this number
print("Compution complete. Largest prime factor for "+str(n)+" is "+str(max(primeFactors)))
# Test values for my thought process. Modulus shows multiple of a number.
# Also shows if number is divisible by a number or itself.
if(13195%5 == 0):
    print("True")

if(7%7==0 and 7%1 ==0):
    print("True")
