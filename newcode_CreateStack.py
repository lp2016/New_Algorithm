# -*- coding:utf-8 -*-
#思路：这道题的要求是在O（1）时间确定栈的最小元素
#      因此要利用一个辅助栈
#      辅助栈记录最小的栈元素：若push的元素a小于等于当前最小元素那么也将a push到辅助栈
#      出栈时，若出栈的元素和最小元素相等则同时出栈辅助栈元素
class Solution:
    def __init__(self):
        self.top=-1
        self.top2=-1
        self.data=[]
        self.data2=[]
        self.minD=32767
    def push(self, node):
        self.top+=1
        self.data.append(node)
        if node<=self.minD:
            self.minD=node
            self.data2.append(node)
            self.top2+=1
        # write code here
    def pop(self):
        # write code here
        tmp=self.data[self.top]
        if tmp == self.minD:
            del self.data2[self.top2]
            self.top2 -= 1
        del self.data[self.top]
        self.top-=1
        return tmp
    def top(self):
        # write code here
        return self.data[self.top]
    def Min(self):
        # write code here
        return self.data2[self.top2]
t=Solution()
t.push(3)
t.push(4)
t.push(2)
t.push(3)
t.pop()
t.pop()
t.pop()
t.push(0)
print(t.Min())