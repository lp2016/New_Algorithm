# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n == 0:
            return 0
        sumD = 0
        for i in range(1, n + 1):
            num = str(i)
            for j in range(0, len(num)):
                if num[j] == '1':
                    sumD += 1
        return sumD


print(Solution().NumberOf1Between1AndN_Solution(1))