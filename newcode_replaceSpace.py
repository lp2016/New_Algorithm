# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s.replace(' ','%20')
Solution().replaceSpace("hello world")