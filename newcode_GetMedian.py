# -*- coding:utf-8 -*-
#思路：注意是数据流的中位数，显然每次读入一个数据后，重新排序后找出中位数的效率很低
#仔细分析：利用两个堆，一个大根堆，一个小根堆
from heapq import heappop,heappush
class Solution:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.count = 1
    def Insert(self, num):
        if self.count == 1:
            heappush(self.maxheap, -num)
        elif self.count % 2 == 0:
            if num < -self.maxheap[0]:
                heappush(self.minheap,-heappop(self.maxheap))
                heappush(self.maxheap,-num)
            else:
                heappush(self.minheap,num)

        else:
            if num > self.minheap[0]:
                heappush(self.maxheap, -heappop(self.minheap))
                heappush(self.minheap, num)
            else:
                heappush(self.maxheap, -num)
        self.count += 1
        # write code here
    def GetMedian(self,n):
        # write code here
        if self.count % 2 == 0:
            return -self.maxheap[0]
        else:
            return float(self.minheap[0] - self.maxheap[0])/2

