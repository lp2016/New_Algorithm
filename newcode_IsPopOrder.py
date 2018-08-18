# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) == 0:
            return False
        if len(pushV) == 1:
            return True
        self.data=pushV
        self.top=len(pushV)-1
        self.data2.append(self.data[self.top])
        self.top-=1
        for item in popV:
            if item == self.data[self.top]:
                self.top -= 1
            else:
                if self.data2 ==[] :
                    return False
                if item in self.data2:
                    del self.data2[self.data2.index(item)]
                    self.top2-=1
                else:
                    self.data2.append(self.data[self.top])
                    self.top -= 1

        return True
    def __init__(self):
        self.top = -1
        self.top2 = -1
        self.data = []
        self.data2 = []
t=Solution()
print(t.IsPopOrder([1,2,3,4,5],[3,4,5,2,1]))