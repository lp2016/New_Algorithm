n,m = input().split()
n = int(n)
m = int(m)
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()
if len(A) == 0:
    print(B)
elif len(B) == 0:
    print(A)
else:
    res = []
    i = j = 0
    if A[0] > B[0]:
        j = 1
        res.append(B[0])
    else:
        i = 1
        res.append(A[0])
    k = 1
    while i < len(A) and j < len(B):
        tmp = 0
        if A[i] > B[j]:
            tmp = B[j]
            j += 1
        elif A[i] <= B[j]:
            tmp = A[i]
            i += 1
        if tmp > res[k - 1]:
            res.append(tmp)
            k += 1

    while i < len(A):
        if A[i] > res[k - 1]:
            res.append(A[i])
            k += 1
        i += 1
    while j < len(B):
        if B[j] > res[k - 1]:
            res.append(B[j])
            k += 1
        j += 1
for i in range(0,len(res)-1):
    print(res[i],end = " ")
print(res[len(res)-1],end ="")
