
def partion(i,j,a):
    n = len(a)
    while i < j :
        while i < j and a[i] <= a[j]:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
        while i < j and a[i] <= a[j]:
            i += 1
        if i < j :
            a[i],a[j] = a[j],a[i]
            j -= 1
    return i  #返回中轴值的下标
if __name__ == "__main__":
    a = [23,13,49,6,31,19,28]
    i = partion(0,len(a)-1,a)
    print(a)