import sys
sys.setrecursionlimit(1000000)
from functools import reduce
class swapsort:
    def largestNumber(self, nums):
        # write code here
        if len(nums) == 0:
            return ""
        numbers = list(map(str, nums))
        self.quicksort(0,len(numbers)-1,numbers)
        result = reduce(lambda x, y: x + y, numbers)
        result = ''.join(result).lstrip('0')
        return result or '0'
    def quicksort(self,start,end,data):
        if start >=end:
            return
        key = self.onesort(start, end, data)
        self.quicksort(start, key - 1, data)
        self.quicksort(key + 1, end, data)
    def onesort(self,start,end,data):
        i=start
        j=end
        key=data[start]
        while i<j:
            while i<j and data[j]+key<=key+data[j]:
                j-=1
            if data[j]+key>key+data[j]:
                data[i],data[j]=data[j],data[i]
                i+=1
            while i<j and data[i]+key>=key+data[i]:
                i+=1
            if data[i]+key<key+data[i]:
                data[i],data[j]=data[j],data[i]
                j-=1
        return i

print(swapsort().largestNumber([3, 30, 34, 5, 9]))
