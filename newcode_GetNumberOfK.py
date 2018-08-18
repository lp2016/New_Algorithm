#思路：显然O（N）时间复杂度不满足要求，那么需要考虑时间复杂度为O（Log N）时间复杂度的算法
#二分查找序列中第一个等于k的位置
#二分查找序列中最后一个等于k的位置
#注意考虑序列中不存在k的情况
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return int(self.LastNumber(data, k) - self.FirstNumber(data, k) + 1)

    def FirstNumber(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] == k:
                if mid == 0:
                    return mid
                if data[mid-1] != k:
                    return mid
                high = mid - 1
            elif k < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return 0.5

    def LastNumber(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] == k:
                if  mid == len(data) - 1:
                    return mid
                if data[mid + 1] != k:
                    return mid
                low = mid + 1
            elif k < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -0.5




print(Solution().GetNumberOfK([1,2,2,2,3],2))