# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number < 4:
            return number
        f = [0]*(number+1)
        f[1] = 1
        f[2] = 2
        f[3] = 3
        for i in range(4, number+1):
            f[i] = f[i-2] * 2 + f[i-3]
        return f[number]