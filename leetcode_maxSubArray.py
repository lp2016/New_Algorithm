class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumD=0
        maxD=float("-Inf")
        for num in nums:
            sumD = sumD + num
            maxD = max(maxD, sumD)
            if sumD < 0:
                sumD = 0
        return maxD

    def maxSubArray_dp(self, nums):
        dp=nums
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)



print(Solution().maxSubArray_dp( [-2,1,-3,4,-1,2,1,-5,4]))



