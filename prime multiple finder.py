import math
print("Number to find prime of: ")
num = int(input())
rootNum = 4*(math.sqrt(num))
roundedNum = int(rootNum) #sets up the variables, converts the float root to an int for processing

primes = [] #sets a list of 'base primes'
factors = [] #empty list of factors that will be filled in later
 #sets i to 8 as the last prime was 7

#if the square root of the original number is even, make it odd by subtracting one
lastDigits = []
oddNumbers = []
def primeNumCheck(x):
    if x >= 2:
        for otherNum in range (2, x):
            if not ( x % otherNum):
                return False
    else:
        return False
    return True
for y in range (2, roundedNum):
    if y%2 !=0 and y%3 !=0 and y%5 !=0 and y%7 !=0:
        oddNumbers.append(y)

for y in oddNumbers:
    if primeNumCheck(y):
        primes.append(y)

#for every number in the primes list, check if its a factor of the original number
if num in {2, 3, 5, 7}:
    print(str(num) + " is a prime number.")
elif num in {0, 1}:
    print("Number is 0 or 1, undefined.")
elif primeNumCheck(num) == True:
    print(str(num) + " is a prime.")
else:
    for x in primes:
        if num%x == 0:
            factors.append(x)
    print("The prime factors of " + str(num) + " are: ")
    print(factors)
    print("The highest prime of " + str(num) + " is: ")
    print(factors[-1:])
    