#arc 邻接矩阵
#v   源点
def dijkstra(arc, v):
    n = len(arc)
    dist = []    #dist[i] 节点v到第i个节点的距离
    maxd = float("Inf")
    path = []
    s = [v]
    visit = [False]*n
    visit[v] = True
    for i in range(0,n):
        dist.append(arc[v][i])
        if arc[v][i] == maxd:
            path.append("")
        else:
            path.append(str(v)+str(i))
    num = 1
    while num < n:
        k = 0
        mind = maxd
        for i in range(0,n):
            if not visit[i] and dist[i] < mind:
                mind = dist[i]
                k = i
        s.append(k)
        visit[k] = True
        for i in range(0,n):
            if dist[i] > dist[k] + arc[k][i]:
                dist[i] = dist[k] + arc[k][i]
                path[i] = path[k] + str(i)
        num = num + 1
    return dist,path
if __name__ == "__main__":
    maxd = float("Inf")
    arc = [[0, 10, maxd, 30, 100],
           [10, 0, 50, maxd, maxd],
           [maxd, 50, 0, 20, 10],
           [30, maxd, 20, 0, 60],
           [100, maxd, 10, 60, 0]
           ]
dist,path = dijkstra(arc,0)
print(dist)
print(path)