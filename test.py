def CompletePack_恰好装满方案总数(V, weight):  # hdu1398,hdu1284
    F = [0] * (V + 1)
    F[0] = 1
    for i in range(0, len(weight)):
        for v in range(weight[i], V + 1):
            F[v] = F[v] + F[v - weight[i]]
    return F[V]
print(CompletePack_恰好装满方案总数(4,[1,2,3]))