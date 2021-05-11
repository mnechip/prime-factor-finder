import math

lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
maxNum = 9007199254740991
factorArray = []

class getFactors:
    def getFactors(self, Num):
        numLeft = Num
        if Num > maxNum:
            return factorArray
        if numLeft == 0 or numLeft == 1:
            return factorArray
        else:
            doneQ = False
            for p in range (0, lowPrimes[-1]):
                p += 1
                if tF.testFactors(lowPrimes[p-1]):
                    doneQ = True
                    break
            if doneQ:
                fact = math.trunc(lowPrimes[p-1] + 5/6)*6-1
                while True:
                    if tF.testFactors(fact):
                        break
                    fact += 2
                    if tF.testFactors(fact):
                        break
                    fact += 4
            #if numLeft != 1:
             #   aF.addFactor(numLeft, 1)
        return factorArray
f = getFactors()

class testFactor:      
    def testFactors(self, factor):
        power = 0
        numLeft = Num
        while (numLeft % factor == 0):
            power += 1
            numLeft = numLeft / factor
        if power != 0:
            aF.addFactor(factor, power)
        return numLeft / factor <= factor
tF = testFactor()

class addFactor:
    def addFactor(self, factor, power):
        for i in range (0, power):
            factorArray.append(factor)
aF = addFactor()

while True:
    Num = int(input("Number: "))
    numLeft = Num
    if not Num < 2 or Num > maxNum:
        f.getFactors(Num)
        print(factorArray)
        break
    else:
        print("You have made an invalid choice.")