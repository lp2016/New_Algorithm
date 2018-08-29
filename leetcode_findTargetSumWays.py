#dfs超时
class Solution:
    def __init__(self):
        self.count = 0
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        self.findTargetSumWaysHelper(0, nums, S, 0)
        return self.count
    def findTargetSumWaysHelper(self, level, nums, S, sumd):
        if level == len(nums):
            if sumd == S:
                self.count += 1
            return
        sumd = sumd + nums[level]
        self.findTargetSumWaysHelper(level+1, nums, S, sumd)
        sumd = sumd - nums[level]
        sumd = sumd - nums[level]
        self.findTargetSumWaysHelper(level + 1, nums, S, sumd)
        sumd = sumd + nums[level]

    def findTargetSumWays_2(self, nums, S):
        tmp = S+sum(nums)
        target = tmp // 2
        if tmp %2 == 1 or S > target:
            return 0
        dp = [[0 for j in range(0,target+1)] for i in range(0,len(nums))]
        for j in range(0,target+1):
            if nums[0] == j:
                dp[0][j] = 1
        dp[0][0] = 1
        for i in range(1,len(nums)):
            for j in range(nums[i],target+1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        res = 0
        for i in range(0,len(nums)):
            res = max(res,dp[i][target])
        return res







print(Solution().findTargetSumWays_2([0,0,0,0,0,0,0,0,1],1))