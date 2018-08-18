# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum == 1:
            return []
        res = []
        tmp = [0]*tsum
        i = 1
        j = 1
        sumD = 0
        while j < tsum:
            if sumD < tsum:
                sumD = sumD + j
                j += 1
            if sumD == tsum:
                res.append(list(range(i, j)))
                sumD = sumD - i
                i += 1
            if sumD > tsum:
                sumD = sumD - i
                i += 1
        return res
print(Solution().FindContinuousSequence(9))





