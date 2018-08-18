
def sum10(n):
    sumd = 0
    while n != 0:
        sumd += n % 10
        n = n // 10
    return sumd
def sum2(n):
    sumd = 0
    while True:
        if n == 1:
            break
        sumd += n % 2
        n = n // 2

    return sumd + 1

n = int(input())
count = 0
for i in range(1,n+1):
    if sum2(i) == sum10(i):
        count += 1
print(count)
