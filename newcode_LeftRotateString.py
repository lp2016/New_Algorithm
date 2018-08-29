#思路：三次翻转
#第一次： 先翻转前n个字符
#第二次：翻转 剩下的字符
#翻转全部字符
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString2(self, s, n):
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

    def LeftRotateString(self, s, n):
        if len(s) == 0 or n > len(s):
            return ""
        s = list(s)
        s1 = s[0:n]
        s2 = s[n:]
        s1 = s1[::-1]
        s2 = s2[::-1]
        s = (s1 + s2)[::-1]
        return "".join(s)

print(Solution().LeftRotateString("abcXYZdef",10))