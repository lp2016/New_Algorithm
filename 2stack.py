# -*- coding:utf-8 -*-
#解题思路：
#入队：直接入栈2
#出队：如果栈1中有元素，直接从栈1出栈一个元素；否则将栈2中所有元素push到栈1中，然后从栈1出栈一个元素
class stack:
    def __init__(self):
        self.top = -1
        self.data=[]
    def pop(self):
        k=self.data[self.top]
        self.top=self.top-1
        del self.data[self.top+1]
        return k
    def push(self,x):
        self.top=self.top+1
        self.data.append(x)

class Solution:
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()
    def push(self, node):
       self.s2.top+=1
       self.s2.data.append(node)
    def pop(self):
        if self.s1.top == -1 :
            while self.s2.top>=0:
                self.s1.push(self.s2.pop())
            return self.s1.pop()
        else:
            return self.s1.pop()



