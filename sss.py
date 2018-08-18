

from math import gcd
def calcSumOfANumber(number):
    total = 0
    for i in range(2,number):
        res, num = 0, number
        while num:
            res += num % i
            num = num // i
        total += res
    return total
while True:
    try:
        a = int(input())
        b = calcSumOfANumber(a)
        gcdRes = gcd(b, a - 2)
        print(str(b // gcdRes) + "/" + str((a - 2) // gcdRes))
    except:
        break