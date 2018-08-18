#思路：动态规划
# maxd[i][j] 表示以第i个人结尾，共个j人时的最大乘积，因为存在负数，所以需要记录最小乘积
# mind[i][j] 表示以第i个人结尾，共个j人时的最小乘积
#转移方程：maxd[i][j] = max(maxd[i][j],maxd[p][j-1]*a[i],mind[p][j-1]*a[i])
n = int(input())
a = list(map(int,input().split()))
k,d = input().split()
k = int(k)
d = int(d)
maxd = [[0 for i in range(0,k)] for j in range(0,n)]
mind = [[0 for i in range(0,k)] for j in range(0,n)]

for i in range(0,n):
    maxd[i][0] = a[i]
    mind[i][0] = a[i]
mm = 0
for i in range(0,n):
    for j in range(1,k):
        p = i - 1
        while p >=0 and p >= i - d:
            maxd[i][j] = max(maxd[i][j],max(maxd[p][j-1]*a[i],mind[p][j-1]*a[i]))
            mind[i][j] = min(mind[i][j],min(maxd[p][j-1]*a[i],mind[p][j-1]*a[i]))
            p -= 1
    mm = max(mm,maxd[i][k-1])
res = -float("Inf")
for  i in range(0,n):
    res = max(res,maxd[i][k-1])
print(res)
print(mm)
