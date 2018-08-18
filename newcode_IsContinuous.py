# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        minD = 20
        for item in numbers:
            if item != 0:
                minD = min(minD,item)
        i = 1
        while i <= 4:
            if minD + i not in numbers:
                if 0 not in numbers:
                    return False
                numbers.remove(0)
            i += 1
        return True



print(Solution().IsContinuous([1,0,0,7,0]))