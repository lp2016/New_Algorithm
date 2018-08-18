# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        tmp = [i for i in range(0,n)]
        i = 0
        count = 0
        while True:
            if i%n in tmp:
                if count == m-1:
                    tmp.remove(i%n)
                    if len(tmp) == 1:
                        return tmp[0]
                    count = 0
                else:
                    count += 1
            i += 1
print(Solution().LastRemaining_Solution(7,3))



