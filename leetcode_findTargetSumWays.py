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

print(Solution().findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0))