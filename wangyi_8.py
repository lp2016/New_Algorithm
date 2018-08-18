#思路：回溯法，子集问题
def dfs(tmp,visit,n,count,w,v):   #w[0]保存剩余容量
    if tmp ==n:
        return
    for i in range(tmp,n):
        if not visit[i] and w[0]>=v[i]:
            visit[i]=True
            w[0]=w[0]-v[i]
            count[0]+=1
            dfs(i+1,visit,n,count,w,v)
            visit[i]=False
            w[0]=w[0]+v[i]
if __name__ == '__main__':
    data = input("")
    n, w = data.split(" ")
    n = int(n)
    w = int(w)
    v = input("")
    v = list(map(int, v.split(" ")))
    if sum(v) <= w:  # 如果所有物品的重量和小于背包容量，就是求所有的子集（2^n），没这个的话会超时，百分之八十AC
        print(2 ** n)
    else:
        visit = [False] * n
        count = [1]
        w1 = [w]
        dfs(0, visit, n, count, w1, v)
        print(count[0])







