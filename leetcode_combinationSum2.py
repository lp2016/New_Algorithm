#思路 ：回溯法
#需要记录路径，同时需要去重
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        sumD =0
        tmp = []
        candidates.sort()                           #首先得排序
        self.combinationSum2Helper(candidates, target, 0, tmp, sumD, res)
        return res

    def combinationSum2Helper(self, candidates, target, start, tmp, sumD, res):
        prev = -1                                   #prev用于记录上一个访问的元素，
        for i in range(start,len(candidates)):
            if i > 0 and candidates[i] == prev:     #保证去重，是为了避免同一层中的重复元素
                continue
            else:
                sumD += candidates[i]
                if sumD <= target:
                    tmp.append(candidates[i])
                    if sumD == target:
                        res.append(tmp[:])
                    self.combinationSum2Helper(candidates, target, i + 1, tmp, sumD, res)
                    tmp.pop()
                    prev = candidates[i]
                sumD = sumD - candidates[i]




print(Solution().combinationSum2( [2,5,2,1,2],5))