def binSearch(low,high,key,data):
    if low == high:
        return -1
    mid=int((low+high)/2)
    if key == data[mid]:
        return mid
    if key <data[mid]:
        index=binSearch(low,mid,key,data)
    else:
        index=binSearch(mid+1,high,key,data)
    return index


a=[0,2,4,6,8,10]
print(binSearch(0,len(a)-1,11,a))



