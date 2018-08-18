
#思路：首先平均数必须是整数
# 如果平均数是奇数，则所有的数都应该是奇数，因为奇数加2减2之后才能是奇数，
# 然后 需要移动的只是大于平均数的数，移动的次数等于(a[i] - avg) //2
# 平均数是偶数的情况同样处理

n = int(input())
a = list(map(int,input().split()))
sumd = sum(a)
if sumd % n :
    print(-1)
else:
    avg = sumd // n
    if avg % 2 == 0:
        work = 0
        count = 0
        for i in range(0,len(a)):
            if a[i] % 2 == 1:
                print(-1)
                work = 1
                break
        if work == 0:
            for i in range(0,n):
                if a[i] > avg:
                    count = count + (a[i] - avg) // 2
            print(count)
    else:
        work = 0
        count = 0
        for i in range(0,len(a)):
            if a[i] % 2 == 0:
                print(-1)
                work = 1
                break
        if work == 0:
            for i in range(0,n):
                if a[i] > avg:
                    count = count + (a[i] - avg) // 2
            print(count)

