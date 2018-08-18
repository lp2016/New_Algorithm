# -*- coding:utf-8 -*-
#思路：回溯法解决
# 注意：一定要先排序
class Solution:

    def subsetsWithDup(self, nums):
        # write code here
        if len(nums) == 0:
            return []
        else:
            res = [[]]
            nums.sort()    #一定要先排序
            self.subsetsWithDupHelper(nums, 0, 0, [], res)
            return res
    def subsetsWithDupHelper(self, nums, level, start, path, res):
        if level == len(nums):
            return
        prev = -1
        for i in range(start,len(nums)):
            if i > 0 and nums[i] == prev:
                continue
            path.append(nums[i])
            res.append(path[:])
            self.subsetsWithDupHelper(nums, level+1, i+1, path, res)
            prev = nums[i]
            path.pop()


print(Solution().subsetsWithDup([4,4,4,1,4]))