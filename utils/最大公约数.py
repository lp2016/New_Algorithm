def gcd(m,n):
    if m < n:
        m,n = n,m
    if m % n == 0:
        return n
    p = m // n
    r = m % n
    return gcd(n,r)