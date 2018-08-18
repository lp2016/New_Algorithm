# -*- coding:utf-8 -*-
#思路：先利用列表的前k个数建立一个大根堆
#   然后将剩下的n-k个数依次和堆顶比较，如果小于堆顶元素，则替换掉原来的堆顶元素，然后重新建堆
#   最终，堆中的元素就是最小的k个数，然后将这k个数排序，返回
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        n=len(tinput)
        if k>n or k<=0:
            return []
        r=tinput[0:k]
        self.Construct_heap(r)
        for j in range(k,n-1):
            if tinput[j]<r[0]:
                r[0]=tinput[j]
                self.Sift(0,k,r)
        self.heap_sort(r)
        return r
    def heap_sort(self,r):
        self.Construct_heap(r)
        n=len(r)
        for i in range(0,n-1):
            r[0],r[n-1-i]=r[n-1-i],r[0]
            self.Sift(0,n-1-i,r)
    def Construct_heap(self,tinput):
        n=len(tinput)
        for i in range(n//2-1,-1,-1):
            self.Sift(i,n,tinput)
    def Sift(self,k,m,tinput):
        i=k
        j=2*k
        while j<m:
            if j<m-1 and tinput[j]<tinput[j+1]:
                j+=1
            if tinput[i]<tinput[j]:
                tinput[i],tinput[j]=tinput[j],tinput[i]
            else:
                break
            i=j
            j=2*i
Solution().GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4)