def jinzhi_sum(n,A):
    count = 0
    tmp = A
    while A >= n:
        count += A % n
        A = A // n
    return count + A
def gcd(m,n):
    if m < n:
        m,n = n,m
    if m % n == 0:
        return n
    p = m // n
    r = m % n
    return gcd(n,r)



try:
    while True:
        A = int(input())
        sumd = 0
        for i in range(2, A):
            sumd += jinzhi_sum(i, A)
        num = gcd(sumd,A-2)
        print(str(sumd//num) + "/" + str((A - 2)//num))
except EOFError:
    pass

