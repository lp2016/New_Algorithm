class MultiplePack:

    def MultiplePack_最大价值(self, V, weight, value, num):
        n = len(weight)
        v = []
        w = []
        for i in range(0, n):
            count = num[i]
            c = count
            k = 0
            while 2 ** k < count:
                v.append(value[i] * 2 ** k)
                w.append(weight[i] * 2 ** k)
                count = count - 2 ** k
                k = k + 1
            v.append(value[i] * (c - 2 ** k + 1))
            w.append(weight[i] * (c - 2 ** k + 1))
        weight = w
        value = v
        F = [0] * (V + 1)
        for i in range(0, n):
            for v in range(V, weight[i] - 1, -1):
                F[v] = max(F[v], F[v - weight[i]] + value[i])
        return F[V]

MultiplePack().MultiplePack_最大价值(10, [5,8], [2,7],[3,13])