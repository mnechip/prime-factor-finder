import math
print("Number to find prime of: ")
num = int(input())
rootNum = math.sqrt(num)
roundedNum = int(rootNum) #sets up the variables, converts the float root to an int for processing

primes = [2,3,5,7] #sets a list of 'base primes'
factors = [] #empty list of factors that will be filled in later
i = 8 #sets i to 8 as the last prime was 7

#if the square root of the original number is even, make it odd by subtracting one
if roundedNum%2 != 0:
    oddRounded = roundedNum - 1
else:
    oddRounded = roundedNum

#for every integer in the range of 8 to SQRT(Original), check if it is a prime by testing divisibility by base primes
for i in range (i, oddRounded):
    if i%2 !=0:
        if i%3 !=0:
            if i%5 !=0:
                if i%7 !=0:
                        primes.append(i) #if it is a prime, append it to the list of primes that range between 2 - SQRT

#for every number in the primes list, check if its a factor of the original number
for i in primes:
    if num%i == 0:
        factors.append(i)
        print("The prime factors of " + str(num) + " are: ")
        print(factors)
        print("The highest prime of " + str(num) + " is: ")
        print(factors[-1])
    elif i == num:
        print(str(num) + " is a prime.")
        
    