n=int(input())
tmp = []
for i in range(0,n):
    t = int(input())
    tmp.append(t)
W=100
v = tmp
w = tmp
dp =[[0 for j in range(0,W + 1)]for i in range(0,n)]
G = [[0 for j in range(0,W + 1)]for i in range(0,n)]
for i in range(0,n):
    for j in range(w[i],W+1):
        if dp[i-1][j]>dp[i-1][j-w[i]]+v[i]:
            G[i][j]=0
            dp[i][j]=dp[i-1][j]
        else:
            G[i][j]=1
            dp[i][j] = dp[i - 1][j-w[i]]+v[i]
i = n-1
j =W
tt=[]
while i>=0:
    if G[i][j]== 0:
        pass
    else:
        tt.append(i)
        j=j-w[i]
    i= i -1
print(len(tt))
for i in range(len(tt)-1,-1,-1):
    print(tt[i]+1)
#测试用例
