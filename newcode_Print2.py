# -*- coding:utf-8 -*-
#思路：利用一个空结点标记当前层完全访问了
# 这种方法也可以用于确定每一个结点所在的层数
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        path = []
        q = deque()
        q.append(pRoot)
        q.append(None)
        while len(q) > 0:
            tmp = q.popleft()
            if tmp is not None:
                path.append(tmp.val)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            else:
                res.append(path[:])
                if len(q) == 0:
                    break
                q.append(None)
                path = []
        return res




a5 = TreeNode(5)
a7 = TreeNode(7)
a9 = TreeNode(9)
a11 = TreeNode(11)

a6 = TreeNode(6)
a8= TreeNode(8)
a10 = TreeNode(10)

a6.left = a5
a6.right = a7

a10.left = a9
a10.right = a11

a8.left = a6
a8.right = a10

print(Solution().Print(a8))