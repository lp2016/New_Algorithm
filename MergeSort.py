def Merge(r, r1, s, m, t):  #合并两个有序序列
    i = s
    j = m + 1
    while i <= m and j <= t:
        if r[i] < r[j]:
            r1[s] = r[i]
            i += 1
        else:
            r1[s] = r[j]
            j += 1
            print(s)
            print(r[j])
        s += 1
    while i <= m:
        r1[s] = r[i]
        i += 1
        s += 1

    while j<= t:
        r1[s] = r[j]
        j += 1
        s += 1
        print('dada')

def MergePass(r, r1, n, h):   #一趟归并程序
    pass

def MergeSort1():
    pass

def MergeSort2(r, r1, s, t):
    if s == t:
        r1[s] = r[s]
    else:
        m = (s + t) // 2
        MergeSort2(r, r1, s, m)
        MergeSort2(r, r1, m+1, t)
        r1 = r[:]
        Merge(r1, r, s, m, t)
r = [1,2,3,4,5,6,7,0]
r1 = [0]*8
MergeSort2(r, r1, 0, 7)
print(r)
print(r1)


