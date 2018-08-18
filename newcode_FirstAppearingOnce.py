# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ""
        self.res = {}


    def FirstAppearingOnce(self):
        # write code here
        for item in self.s:     #注意，此处是遍历原字符串，如果遍历字典，碰到的第一个value等于1的字符可能不是真正的第一个，因为字典是无序的
            if self.res[item] == 1:
                return item
        return "#"

    def Insert(self, char):
        # write code here
        self.s = self.s + char
        if char not in self.res:
            self.res[char] = 1
        else:
            self.res[char] += 1


print(Solution().Insert("aagoogle"))