tmp= input().split(" ")
N = int(tmp[0])
W = int(tmp[1])
V= []  #物品价值
w = [] #物品重量
for i in range(1,N+1):
    tmp = input().split(" ")
    weight = int(tmp[0])
    value = int(tmp[1])
    count = int(tmp[2])
    c = count
    k = 0
    while 2**k < count:
        V.append(value * 2**k)
        w.append(weight * 2**k)
        count = count - 2**k
        k = k + 1
    V.append(value * (c - 2**k + 1))
    w.append(weight * (c - 2**k + 1))
dp = [0]*(W + 1)
for i in range(0,len(w)):
    for v in range(W,V[i]-1,-1):
        dp[v] = max(dp[v],dp[v-w[i]]+V[i])

print(max(dp))



