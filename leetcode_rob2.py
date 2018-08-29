#解题思路：动态规划
#就是打家劫舍I的基础之上稍微改变，只不过加了个限制条件：不能同时打劫第一家和最后一家
#那么最优的方案肯定在以下两种情况中：
#（1）从第一家到倒数第二家进行打劫
#（2）从第二家到倒数第一家进行打劫
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        if n == 3:
            return max(nums[0],max(nums[1],nums[2]))
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        res = 0
        for i in range(2,n - 1):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        res = max(res,dp[n-2])
        dp[1] = nums[1]
        dp[2] = max(nums[1],nums[2])
        for i in range(3,n):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        res = max(res,dp[n-1])
        return res
print(Solution().rob([1,2,3,1]))
