# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array)==0:
            return []
        res =[]
        for i in range(0,len(array)):
            if self.Bfind(tsum-array[i],array[i+1:]):
                if array[i]<=tsum-array[i]:
                    return [array[i]]+[tsum-array[i]]
                else:
                    return [tsum-array[i]]+[array[i]]
        return []
    def Bfind(self,target,array):
        low=0
        high=len(array)-1
        while low<= high:
            mid=(low+high)//2
            if target == array[mid]:
                return True
            elif target<array[mid]:
                high=mid-1
            else:
                low=mid+1
        return False
print(Solution().FindNumbersWithSum([1,2,3,4,5,6],7))




