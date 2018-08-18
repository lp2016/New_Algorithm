# -*- coding:utf-8 -*-
#思路：利用双端队列，只把有可能成为滑动窗口最大值的数值存入双端队列
#首先计算第一个窗口的最大值，将窗口每一个数和队列中的每一个数作比较（从队尾开始）
#如果比队列中元素大则删除队列中元素，因为队列中这个元素A不可能是最大值
#接着滑动窗口，步骤和上述基本相同，只有一点不同
#需要监测队头元素是否还在当前窗口内，方法是：利用当前遍历的下标减去窗口size
from collections import  deque
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num:
            return []
        if size > len(num) or size < 1:
            return []
        q = deque()
        res = []
        q.append(0)
        for i in range(1, size):
            while len(q) > 0 and num[i] >= num[q[-1]]:
                q.pop()
            q.append(i)
        res.append(num[q[0]])
        for i in range(size, len(num)):
            while len(q) > 0 and num[i] >= num[q[-1]]:
                q.pop()
            if len(q) > 0 and i - q[0] >= size:
                q.popleft()
            q.append(i)
            res.append(num[q[0]])
        return res
print(Solution().maxInWindows([2,3,4,2,6,2,5,1],3))
