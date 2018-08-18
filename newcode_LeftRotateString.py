#思路：三次翻转
#第一次： 先翻转前n个字符
#第二次：翻转 剩下的字符
#翻转全部字符
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if n > len(s) :
            return ""
        res = list(s)
        self.ReverseSentence(res, 0, n - 1)
        self.ReverseSentence(res, n, len(res) - 1)
        self.ReverseSentence(res, 0, len(res) - 1)
        return ''.join(res)

    def ReverseSentence(self, res, start, end):
        j = end
        k = 0
        for i in range(start,(start + end + 1) // 2 ):
            res[i],res[j-k] = res[j-k],res[i]
            k += 1
        return ' '.join(res)

print(Solution().LeftRotateString("abcXYZdef",3))