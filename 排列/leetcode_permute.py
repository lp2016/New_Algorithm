# -*- coding:utf-8 -*-
#思路：回溯法，全排列问题
class Solution:

    def permute(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        else:
            visit = [False] * len(ss)
            res = []
            self.PermutationHelper(ss, 0, [], visit, res)
            return res
    def PermutationHelper(self,ss, level, path, visit, res):
        if level == len(ss) :
            res.append(path[:])       #此处注意
            return
        for i in range(0,len(ss)):    #排列问题，在每一层需要遍历全部元素
            if  visit[i]:
                continue
            path.append(ss[i])
            visit[i] = True
            self.PermutationHelper(ss, level + 1, path, visit, res)
            path.pop()
            visit[i] = False


print(Solution().permute([1,2,3]))

