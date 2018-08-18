
#思路：第一个和最后一个交换，第二个和倒数第二个交换，依次类推

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        res = s.split(' ')
        j = len(res) - 1
        for i in range(0,len(res) // 2 ):
            res[i],res[j-i] = res[j-i],res[i]
        return ' '.join(res)
print(Solution().ReverseSentence(" "))


