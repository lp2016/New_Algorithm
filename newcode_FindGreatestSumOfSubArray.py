# -*- coding:utf-8 -*-
#思路：依次累加每一个数，当和小于0时，从最新一个数开始累加
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        maxD=array[0]
        sumD=0
        for i in range(0,len(array)):

            if sumD<0:
                sumD=array[i]
            else:
                sumD = sumD + array[i]
            maxD=max(sumD,maxD)
        return maxD
print(Solution().FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))

