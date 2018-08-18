# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        for item in array:
            if target in item:
                return True
        return False

tt=Solution()
print(tt.Find(2,[[1,2],[3,4]]))