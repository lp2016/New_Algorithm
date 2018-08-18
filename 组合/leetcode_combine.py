# -*- coding:utf-8 -*-
#思路：回溯法，组合问题
class Solution:
    def combine(self, n,k):
        # write code here
        if n == 0:
            return []
        else:
            data =[i for i in range(1,n+1)]
            res = []
            self.combineHelper(data, n, k, 0, 0, [], res)
            return res

    def combineHelper(self, data, n, k, start, level, path, res):
        if level == k:
            res.append(path[:])
            return
        for i in range(start, n):
            path.append(data[i])
            self.combineHelper(data, n, k, i+1, level+1, path, res)    #下一层下标从i+1开始，避免[1,1]这种组合
            path.pop()


print(Solution().combine(4,2))