#思路：动态规划
#本质上就是求不相邻数字的最大和
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp=[0]*len(nums)
        dp[0]=nums[0]
        if len(nums)==1:
            return dp[0]
        dp[1]=max(dp[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[len(nums)-1]
print(Solution().rob( [2,3]))

