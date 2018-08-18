#思路 ：回溯法解决     等于某一个数的组合问题
#需要记录路径，同时需要去重
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        sumD =0
        tmp = []
        self.combinationSumHelper(candidates, target, 0, tmp, sumD, res)
        return res

    def combinationSumHelper(self, candidates, target, start, tmp, sumD, res):
        for i in range(start,len(candidates)):
            sumD += candidates[i]
            if sumD <= target:
                tmp.append(candidates[i])
                if sumD == target:
                    res.append(tmp[:])
                # 下一层递归从下标i开始，而不是从下标0开始保证组合不重复，同时保证可重复选取某一个元素，combinationSum的下一层下标从i+1开始使得不可重复使用元素
                self.combinationSumHelper(candidates, target, i, tmp, sumD, res)
                tmp.pop()
            sumD = sumD - candidates[i]




print(Solution().combinationSum( [2,3,6,7],7))