import sys
sys.setrecursionlimit(1000000)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = list(range(0, len(nums)))
        self.quicksort(0, len(nums) - 1, nums, index)
        result = []
        for i in range(0, len(nums)):
            k = self.binSearch(i + 1, len(nums) - 1, target - nums[i], nums)
            if k > 0:
                result.append(index[i])
                result.append(index[k])
                return result

    def quicksort(self, start, end, data,index):
        if start >= end:
            return
        key = self.onesort(start, end, data,index)
        self.quicksort(start, key - 1, data,index)
        self.quicksort(key + 1, end, data,index)

    def onesort(self, start, end, data,index):
        i = start
        j = end
        key = data[start]
        while i < j:
            while i < j and data[j] >= key:
                j -= 1
            if data[j] < key:
                data[i], data[j] = data[j], data[i]
                index[i],index[j]=index[j],index[i]
                i += 1
            while i < j and data[i] <= key:
                i += 1
            if data[i] > key:
                data[i], data[j] = data[j], data[i]
                index[i], index[j] = index[j], index[i]
                j -= 1
        return i

    def binSearch(self,low, high, key, data):
        if low > high:
            return -1

        mid = int((low + high) / 2)
        if key == data[mid]:
            return mid
        if key < data[mid]:
            index = self.binSearch(low, mid-1, key, data)
        else:
            index = self.binSearch(mid + 1, high, key, data)
        return index

    def addTwoSum(self,nums,target):
        index=list(range(0,len(nums)))
        self.quicksort(0,len(nums)-1,nums,index)
        result = []
        for i in range(0, len(nums)):
            k=self.binSearch(i+1,len(nums)-1,target-nums[i],nums)
            if k>0:
                result.append(index[i])
                result.append(index[k])
                return result

