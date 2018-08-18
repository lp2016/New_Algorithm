# -*- coding:utf-8 -*-
#思路：回溯法，全排列问题
#含有重复元素，一定要先排序，和求含有重复元素的子集问题道理一致
class Solution:

    def permuteUnique(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        else:
            visit = [False] * len(ss)
            res = []
            ss.sort()            #一定要先排序
            self.PermutationHelper(ss, 0, [], visit, res)
            return res
    def PermutationHelper(self,ss, level, path, visit, res):
        if level == len(ss) :
            res.append(path[:])       #此处注意
            return
        prev = '1'    #不要把prev设置为-1，因为存在等于-1的元素。。。。
        for i in range(0,len(ss)):    #排列问题，在每一层需要遍历全部元素
            if  visit[i] or ss[i] == prev:
                continue
            path.append(ss[i])
            visit[i] = True
            self.PermutationHelper(ss, level + 1, path, visit, res)
            path.pop()
            visit[i] = False
            prev = ss[i]

print(Solution().permuteUnique([-1,2,-1,2,1,-1,2,1]))

