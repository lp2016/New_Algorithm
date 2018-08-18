n = int(input())
v = []
for i in range(1, n + 1):
    tmp = int(input())
    v.append(tmp)
d = {}
u = []
for i in range(0, len(v)):
    if v[i] not in d:
        d[v[i]] = 1
        u.append(v[i])
if len(u) <= 10:
    print(len(u))
    for i in range(0, len(u)):
        print(u[i])
else:
    print(10)
    for i in range(0, 10):
        print(u[i])





