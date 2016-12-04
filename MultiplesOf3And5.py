"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
i = 0
sum = 0

while (i < 1000):
    if (i % 5 == 0):
        print(str(i)+" is a multiple of 5")

        sum += i


    elif(i % 3 == 0):
        print(str(i)+ " is a multiple of 3")
        sum += i

    i+= 1

print("The sum of multiples bewteen 3 and 5 is "+str(sum))
