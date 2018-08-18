#V:背包容量
#weight：重量
#value：价值
class ZeroOnePack:
    def ZeroOnePack_能否恰好装满(self, V, weight, value):  # 例如leetcode416,此类问题一般只考虑重量
        F = [0] * (V + 1)
        for i in range(0, len(weight)):
            for v in range(V, weight[i] - 1, -1):
                F[v] = max(F[v], F[v - weight[i]] + value[i])
                if F[v] == V:
                    return True
            return False

    def ZeroOnePack_恰好装满的总价值(self, V, weight, value):
        maxD = -float("Inf")
        F = [maxD] * (V + 1)
        F[0] = 0
        for i in range(0, len(weight)):
            for v in range(V, weight[i] - 1, -1):
                F[v] = max(F[v], F[v - weight[i]] + value[i])

    def ZeroOnePack_不要求恰好装满的总价值(self, V, weight, value):
        F = [0] * (V + 1)
        for i in range(0, len(weight)):
            for v in range(V, weight[i] - 1, -1):
                F[v] = max(F[v], F[v - weight[i]] + value[i])
        return F[V]



    def ZeroOnePack_总价值最大的方案数(self, V, weight, value):
        F = [0] * (V + 1)
        G = [1] * (V + 1)
        for i in range(0, len(weight)):
            for v in range(V, weight[i] - 1, -1):
                if F[v] < F[v - weight[i]] + value[i]:
                    F[v] = F[v - weight[i]] + value[i]
                    G[v] = G[v - weight[i]]
                elif F[v] == F[v - weight[i]] + value[i]:
                    G[v] = G[v] + G[v - weight[i]]
        #F[V]表示最大价值，G[V]表示方案数
        return F[V],G[V]

    def ZeroOnePack_恰好装满的方案数(self, V, weight):
        F = [0] * (V + 1)
        F[0] = 1
        for i in range(0, len(weight)):
            for v in range(V, weight[i] - 1, -1):
                F[v] = F[v] + F[v - weight[i]]
        return F[V]

    def ZeroOnePack_记录方案(self, V, weight, value):
        n = len(weight)
        F = [0] * (V + 1)
        visit = [[0 for j in range(0, V + 1)] for i in range(0, n)]
        for i in range(0, n):
            for v in range(V, weight[i] - 1, -1):
                if F[v] < F[v - weight[i]] + value[i]:
                    F[v] = F[v - weight[i]] + value[i]
                    visit[i][v] = 1
        i = n - 1
        j = V
        tt = []  # tt中保存的是选择的物品下标
        while i >= 0:
            if visit[i][j] == 1:
                tt.append(i)
                j = j - weight[i]
            i = i - 1
        return tt
