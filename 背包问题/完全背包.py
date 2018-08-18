class CompletePack:

    def CompletePack_价值最大(self, V, weight, value):
        F = [0] * (V + 1)
        for i in range(0, len(weight)):
            for v in range(weight[i],V+1):
                F[v] = max(F[v], F[v - weight[i]] + value[i])
        return F[V]

    def CompletePack_恰好装满方案总数(self, V, weight):   #hdu1398,hdu1284
        F = [0] * (V + 1)
        F[0] = 1
        for i in range(0, len(weight)):
            for v in range(weight[i],V+1):
                    F[v] = F[v] + F[v - weight[i]]
        return F[V]

    def CompletePack_总价值最大的方案数(self, V, weight, value):
        F = [0] * (V + 1)
        G = [1] * (V + 1)
        for i in range(0, len(weight)):
            for v in range(weight[i],V + 1):
                if F[v] < F[v - weight[i]] + value[i]:
                    F[v] = F[v - weight[i]] + value[i]
                    G[v] = G[v - weight[i]]
                elif F[v] == F[v - weight[i]] + value[i]:
                    G[v] = G[v] + G[v - weight[i]]
        #F[V]表示最大价值，G[V]表示方案数
        return F[V],G[V]