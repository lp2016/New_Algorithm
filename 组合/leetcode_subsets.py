# -*- coding:utf-8 -*-
#思路：回溯法解决
class Solution:

    def subsets(self, nums):
        # write code here
        if len(nums) == 0:
            return []
        else:
            res = [[]]
            self.subsetsHelper(nums, 0, 0, [], res)
            return res
    def subsetsHelper(self, nums, level, start, path, res):
        if level == len(nums):
            return
        for i in range(start,len(nums)):
            path.append(nums[i])
            res.append(path[:])
            self.subsetsHelper(nums, level+1, i+1, path, res)
            path.pop()


print(Solution().subsets([1,2,3]))