#思路：（2,5）的和=（0,5）的和-（0,2）的和+第2个数
class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=nums
        self.I = []
        sumD=0
        for i in range(0,len(nums)):
            sumD=sumD+nums[i]
            self.I.append(sumD)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.I[j]-self.I[i]+self.nums[i]




